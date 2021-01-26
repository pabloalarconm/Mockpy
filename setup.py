# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="mockpy",
    version="0.1.1",
    packages=find_packages(),
    author="Pablo Alarcón Moreno",
    author_email="pabloalarconmoreno@gmail.com",
    url="https://github.com/pabloalarconm/mockpy",
    description="Light-weight Dataframe editor for tidy data management",
    license="MIT",
    keywords="Tidy Dataframe Editor",
    long_description=readme
)