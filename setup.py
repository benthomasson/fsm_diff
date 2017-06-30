#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='fsm_diff',
    version='0.1.0',
    description='Find difference between two finite state machine definitions',
    long_description=readme + '\n\n' + history,
    author='Ben Thomasson',
    author_email='benthomasson@gmail.com',
    url='https://github.com/benthomasson/fsm_diff',
    packages=[
        'fsm_diff',
    ],
    package_dir={'fsm_diff': 'fsm_diff'},
    include_package_data=True,
    install_requires=required,
    license="BSD",
    zip_safe=False,
    keywords='fsm_diff',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    entry_points={
	'console_scripts': [
	    'fsm_diff = fsm_diff.cli:main'
	]
    }
)
