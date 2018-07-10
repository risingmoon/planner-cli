#!/usr/bin/env python

from distutils.core import setup

setup(name='planner',
      version='1.0',
      packages=['planner'],
      install_requires=[
          'requests',
      ],
      entry_points={
          'console_scripts': ['planner = planner.__main__:main']})
