import setuptools


with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "raster",
    version = "0.0.0",
    author = "Shen Pengju",
    author_email = "spjace@sina.com",
    description = "A small package for raster analysis",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/spjace/raster",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)