# -*- coding: utf-8 -*-
"""
setup.py

python-can-canine
"""

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()

setup(
    name="python-can-canine",
    version="0.2.1",
    author="Yannis Chatzikonstantinou",
    author_email="info@tinymovr.com",
    description="Python-can CANine",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yconst/python-can-canine",
    packages=find_packages(include=['canine', 'canine.*']),
    python_requires=">=3.9",
    install_requires=[
        "python-can",
        "pyusb~=1.0"
    ],
    entry_points = {
        'can.interface': [
            'canine = canine.canine:CANineBus'
        ]
    }
)
