import numpy as np
import re
import tifffile as tf
from pathlib import Path
from tqdm import tqdm

def split(tif_path, jumps):
    if isinstance(tif_path, str):
        tif_path = Path(tif_path)

    frameTimestamps_sec = None
    with tf.TiffFile(tif_path) as tif:
        for channels, page in enumerate(tif.pages):
            ft = float(re.findall(r'frameTimestamps_sec = (\d+\.\d+)', page.tags[270].value)[0])
            if frameTimestamps_sec is None:
                frameTimestamps_sec = ft
            if ft != frameTimestamps_sec:
                break
    samples = jumps * channels

    output_paths = [tif_path.parent / f"{tif_path.stem}_{i:04d}{tif_path.suffix}" for i in range(int(jumps))]
    output_handles = [open(f, "wb") for f in output_paths]

    filehandle_map = np.array([list(range(jumps))] * channels).T.flatten()

    # Open the original multipage TIFF file
    with tf.TiffFile(tif_path) as tif, open(tif_path, "rb") as tifh:
        ifd_length = tif.pages[1].offset - tif.pages[0].offset
        data_offset = tif.pages[0].dataoffsets[0] - tif.pages[0].offset

        # Copy header
        for output_tif in output_handles:
            tifh.seek(0)
            output_tif.write(tifh.read(tif.pages[0].offset))

        # Copy pages
        n_pages = len(tif.pages)
        last_start_pos = [0] * int(jumps)
        for i, page in enumerate(tqdm(tif.pages)):
            page_offset = page.offset
            # print(page_offset)

            # Select file to save in
            sample_idx = float(i) / samples
            sample_idx = int((sample_idx - int(sample_idx)) * samples)
            ofh = output_handles[filehandle_map[sample_idx]]

            # Start and end position in new file
            idf_new_start_pos = ofh.tell()
            last_start_pos[filehandle_map[sample_idx]] = idf_new_start_pos
            # print(idf_new_start_pos)
            idf_new_end_pos = idf_new_start_pos + ifd_length

            # Copy the ifd
            tifh.seek(page_offset)
            buffer = tifh.read(ifd_length)
            ofh.write(buffer)

            assert idf_new_end_pos == ofh.tell(), f"We did not end up ({ofh.tell()}) where we expected ({idf_new_end_pos})"

            # Go back to the beginning of the ifd
            tifh.seek(page_offset)

            # Go through the tags and adjust
            n_tags = np.fromfile(tifh, dtype=np.uint64, count=1)[0]
            for i_tag in range(n_tags):
                # Read from source file
                # print(idf_new_start_pos+8+20*i_tag, tifh.tell())
                tag_tag = np.fromfile(tifh, dtype=np.uint16, count=1)[0]
                tag_type = np.fromfile(tifh, dtype=np.uint16, count=1)[0]
                tag_n_values = np.fromfile(tifh, dtype=np.uint64, count=1)[0]
                val_pos_orig = tifh.tell()
                tag_values = np.fromfile(tifh, dtype=np.uint64, count=1)[0]

                # Go to value of the tag in target file ...
                ofh.seek(idf_new_start_pos + 8 + 20 * i_tag + 12)
                # ... and write new value
                val_pos_new = ofh.tell()
                if tag_tag == 273:  # data offset
                    value = np.uint64(idf_new_start_pos + data_offset)
                    # print(f"writing {value} for {tag_values} at {val_pos_new} from {val_pos_orig}")
                    np.array(value).tofile(ofh)
                elif tag_tag == 270:  # image description
                    value = np.uint64(tag_values - page.offset + idf_new_start_pos)
                    # print(f"writing {value} for {tag_values} at {val_pos_new} from {val_pos_orig}")
                    np.array(value).tofile(ofh)
            ofh.seek(int(idf_new_start_pos + 8 + 20 * n_tags))
            np.array(np.uint64(idf_new_end_pos)).tofile(ofh)
            ofh.seek(idf_new_end_pos)

        ofh.seek(int(idf_new_start_pos + 8 + 20 * n_tags))
        np.array(np.uint64(0)).tofile(ofh)

    for i, oh in enumerate(output_handles):
        oh.seek(
            int(last_start_pos[i] + 8 + 20 * n_tags))  # This only works if all ifds have the same amount of tags ...
        np.array(np.uint64(0)).tofile(oh)
        oh.close()
