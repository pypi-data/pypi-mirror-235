from setuptools import setup, find_packages

setup(
    name="memgpt",
    version="0.0.1",
    description="MemGPT python library",
    author="MemGPT",
    author_email="circerebrospinalfluid@gmail.com",
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.8',
    include_package_data=True,
    install_requires = open('requirements.txt').readlines(),
)
