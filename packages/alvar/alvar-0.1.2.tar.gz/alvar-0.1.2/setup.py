from setuptools import setup, find_packages
from io import open


def read(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


setup(
    name="alvar",
    version="0.1.2",
    description="Allan variance calculation",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="sisteralab",
    author_email="ya.vodzyanovskiy@lebedev.ru",
    url="https://github.com/sisteralab/alvar",
    keywords="allan variance",
    packages=find_packages(),
    install_requires=["numpy"],
)
