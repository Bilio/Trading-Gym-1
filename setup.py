#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='tgym',
    version='0.1.0',
    description="Trading Gym is an open-source project for the development of reinforcement learning algorithms in the context of trading.",
    author="Darrick Joo",
    author_email='',
    url='https://github.com/darjoo/trading-gym',
    packages=find_packages(),
    install_requires=[
        'matplotlib==2.0.2'
    ],
    license="MIT license",
    zip_safe=False,
    keywords='tgym'
)
