#!/usr/bin/env python

from distutils.core import setup

setup(name='python-darkcoinrpc',
      version='0.1',
      description='Enhanced version of python-jsonrpc for use with Darkcoin',
      long_description=open('README').read(),
      author='Jeff Garzik',
      author_email='<jgarzik@exmulti.com>',
      maintainer='Vertoe Qhor',
      maintainer_email='<vertoe@qhor.net>',
      url='http://www.github.com/vertoe/python-darkcoinrpc',
      packages=['darkcoinrpc'],
      classifiers=['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'])
