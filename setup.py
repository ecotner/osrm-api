import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="osrm",  # Replace with your own username
    version="0.0.1",
    author="Eric Cotner",
    author_email="2.71828cotner@gmail.com",
    description="A python API for interacting with OSRM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ecotner/osrm-api/",
    packages=["osrm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
