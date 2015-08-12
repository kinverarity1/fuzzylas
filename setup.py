"""Setup script for fuzzylas

Based on:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

from distutils.core import setup


with open(path.join(path.dirname(__file__), "requirements.txt"), "r") as f:
    requirements = f.read().splitlines()

with open(path.join(path.dirname(__file__), "README.rst"), "r") as f:
    README = f.read()

setup(name="fuzzylas",

      version=__version__,

      description="",
      long_description=README,

      url="",

      author="",
      author_email="",

      license="Apache",

      classifiers=[
      ],

      keywords="",

      packages=["fuzzylas", ],

      install_requires=requirements,

      entry_points={
          'console_scripts': [],
      }
      )
