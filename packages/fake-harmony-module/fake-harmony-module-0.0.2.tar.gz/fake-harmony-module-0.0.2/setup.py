from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.2'
DESCRIPTION = 'Fake harmony module'
LONG_DESCRIPTION = """
This repository contains a fake ToonBoom package featuring a Harmony module that includes all the classes used within Harmony's Python interface. Its primary purpose is to provide autocompletion, access to docstrings, and accurate type hints in your preferred IDE.

All classes have been written based on Harmony's Python documentation, which can be found at <https://docs.toonboom.com/help/harmony-22/scripting/pythonmodule/index.html>.

Please note that this fake module may contain inconsistencies, missing return types, and typos. Unfortunately, most of these issues stem from faithfully transcribing Harmony's flawed documentation.
"""

# Setting up
setup(
    name="fake-harmony-module",
    version=VERSION,
    author="Tristan Languebien",
    author_email="<tlanguebien@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=['ToonBoom'],
    install_requires=[],
    keywords=['python', 'toonboom', 'harmony'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)