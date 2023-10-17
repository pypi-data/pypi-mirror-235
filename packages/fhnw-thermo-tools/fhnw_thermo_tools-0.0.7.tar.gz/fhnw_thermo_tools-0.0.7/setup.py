from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fhnw_thermo_tools",
    version="0.0.7",
    author="Raffael Schreiber",
    author_email="raffaelmichael.schreiber@fhnw.ch",
    long_description=long_description,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy~=1.26.1",
        "matplotlib~=3.8.0",
        "coolprop==6.5.0.post1",
    ],
)
