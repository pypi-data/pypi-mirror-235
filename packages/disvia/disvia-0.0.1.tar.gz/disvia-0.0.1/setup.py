from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'Retrieving data from discord via token'
LONG_DESCRIPTION = 'A package that allows to retrieve information about discord via token'

# Setting up
setup(
    name="disvia",
    version=VERSION,
    author="MrWhxte",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'discord'],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
    ]
)
