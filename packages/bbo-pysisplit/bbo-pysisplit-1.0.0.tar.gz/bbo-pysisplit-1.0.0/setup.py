import pathlib
from setuptools import find_packages, setup
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="bbo-pysisplit",
    version="1.0.0",
    description="Split ScanImage TIFFs into multiple files",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bbo-lab/pySIsplit",
    author="BBO-lab @ caesar",
    author_email="kay-michael.voit@mpinb.mpg.de",
    license="LGPL",
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Programming Language :: Python :: 3.10",
    ],
    packages=['sisplit'],
    include_package_data=True,
    install_requires=['numpy', 'tqdm', 'tifffile', 'argparse'],
)
