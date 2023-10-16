import setuptools
from pathlib import Path
setuptools.setup(
    name="zbrojarzpdf",
    version=1.1,
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=["test", "data"])
)
