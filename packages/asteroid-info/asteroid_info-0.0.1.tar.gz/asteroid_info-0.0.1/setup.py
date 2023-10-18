from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="asteroid_info",
    version="0.0.1",
    author="FAM",
    author_email="m.zarantonello2@campus.unimib.it",
    description="Package",
    packages=find_packages(),

    long_description = long_description,
    long_description_content_type = "text/markdown",
    
    license = "MIT",


)