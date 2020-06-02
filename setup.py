#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='chipwhisperer',
    version='5.1.3',
    description="ChipWhisperer Side-Channel Analysis Tool",
    author="Colin O'Flynn",
    author_email='coflynn@newae.com',
    license='GPLv3',
    url='https://www.chipwhisperer.com',
    packages=find_packages('software'),
    package_dir={'': 'software'},
    install_requires=[
        'configobj',
        'pyserial',
        'numpy',
        'pyusb',
        'scipy',
    ],
    python_requires='~=3.4'
)
