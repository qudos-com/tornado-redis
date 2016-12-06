#!/usr/bin/env python
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = re.compile(r'__version__\s*=\s*[\'\"](.+)[\"\']')

def get_package_version():
    "returns package version without importing it"
    base = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base, "tornadoredis/__init__.py")) as initf:
        for line in initf:
            m = version.match(line.strip())
            if not m:
                continue
            return m.groups(1)[0]

setup(name='tornado-redis',
      version=get_package_version(),
      description='Asynchronous Redis client for the Tornado Web Server.',
      author='Vlad Glushchuk',
      author_email='vgluschuk@gmail.com',
      license="http://www.apache.org/licenses/LICENSE-2.0",
      url='http://github.com/leporo/tornado-redis',
      keywords=['Redis', 'Tornado'],
      packages=['tornadoredis'])
