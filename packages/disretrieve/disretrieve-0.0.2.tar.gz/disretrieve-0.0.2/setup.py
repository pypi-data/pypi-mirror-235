from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.2'
DESCRIPTION = 'Retrieving data from discord via token'
LONG_DESCRIPTION = 'A package that allows to retrieve information about discord via token'

# Setting up
setup(
    name="disretrieve",
    version=VERSION,
    author="MrBlxck",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['python', 'discord'],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
    ]
)