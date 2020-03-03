# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup

version = "0.0.1"

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="Jpoc",
    packages=["jpoc"],
    entry_points={

        "console_scripts": ['jpoc = jpoc.bootstrap:main']

    },
    version=version,
    description="Python command line application bare bones.",
    long_description=long_descr,
    author="cah-cesar-medrano",
    author_email="cesar.medrano@cardinalhealth.com",
)
