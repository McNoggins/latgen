#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='latgen',
    version='0.1.0',
    description='Computational library to generate lattice points',
    long_description=readme + '\n\n' + history,
    author='Denis Gagnon',
    author_email='gagnon88@gmail.com',
    url='https://github.com/McNoggins/latgen',
    packages=find_packages(),
    package_dir={'latgen':
                 'latgen'},
    include_package_data=True,
    install_requires=[
      'numpy',
    ],
    license="BSD",
    zip_safe=False,
    keywords='latgen',
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
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
