#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of portolan.
# http://github.com/fitnr/portolan

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from setuptools import setup

try:
    readme = open('README.rst').read()
except IOError:
    try:
        readme = open('README.md').read()
    except IOError:
        readme = ''

setup(
    name='portolan',

    version='1.0.1',

    description="Convert between compass points and degrees",

    long_description=readme,

    url='https://github.com/fitnr/portolan',

    author='Neil Freeman',

    author_email='contact@fakeisthenewreal.org',

    license='GPL',

    packages=['portolan'],

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Intended Audience :: Science/Research',
    ],
)
