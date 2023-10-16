import setuptools
from pathlib import Path
setuptools.setup(
    name="min-max-app",
    version="1.0.0",
    long_description=Path("README.md").read_text(),
    author="Your Name",
    author_email="your@email.com",
    packages=setuptools.find_packages(exclude=["tests","data"])
)
