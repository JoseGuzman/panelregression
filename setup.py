"""
setup.py

Author: Jose Guzman, sjm.guzman@gmail.com 
Created: 01/05/2024

Installation file required for the panelregression  module
"""
import os
import re
import os.path as op
from setuptools import setup 

#-------------------------------------------------------------------------
# setup
#-------------------------------------------------------------------------
def _package_tree(pkgroot):
    path = op.dirname(__file__)
    subdirs = [op.relpath(i[0], path).replace(op.sep, '.')
               for i in os.walk(op.join(path, pkgroot))
               if '__init__.py' in i[2]]
    return subdirs


# read README.md
curdir = op.dirname(op.realpath(__file__))
with open(op.join(curdir, 'README.md')) as f:
    myreadme = f.read()

# Find version number from `__init__.py` without executing it.
filename = op.join(curdir, 'panelregression/__init__.py')
with open(filename, 'r') as f:
    myversion = re.search(r"__version__ = '([^']+)'", f.read()).group(1)


setup(
    name = 'panelregression', # application name
    version = myversion,# application version
    license = 'LICENSE',
    description = 'panelregression is a Python module',
    long_description = myreadme,
    author = 'Jose Guzman',
    author_email = 'sjm.guzman@gmail.com',
    packages = ['panelregression'],
    python_requires='>=3.5',
    include_package_data = True,# include additional data
    package_data={
        # If any package contains *.txt files, include them:
        '': ['*.txt'],
        # And include any *.csv files in the 'datasets' subdirectory
        # of the 'panelregression' package, also:
        'panelregression': ['datasets/*.csv'],
    },
)
