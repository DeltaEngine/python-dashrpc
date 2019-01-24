#!/usr/bin/env python

from distutils.core import setup

setup(name='python-dashrpc',
      version='0.3',
      description='Enhanced version of python-jsonrpc for use with Dash',
      long_description=open('README').read(),
      author='Jeff Garzik',
      author_email='<jgarzik@exmulti.com>',
      maintainer='Benjamin Nitschke',
      maintainer_email='<Benjamin@DeltaEngine.net>',
      url='http://www.github.com/DeltaEngine/python-dashrpc',
      packages=['dashrpc'],
      classifiers=['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'])
