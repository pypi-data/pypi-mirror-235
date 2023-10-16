from setuptools import setup, find_packages

setup(
    name="SpaceGPT",
    version="0.0.1",
    description="SpaceGPT python library",
    author="SpaceGPT Team",
    author_email="silveryfu@gmail.com",
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.8',
    include_package_data=True,
    install_requires = open('requirements.txt').readlines(),
)
