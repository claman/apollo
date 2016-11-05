# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
  name='percival',
  version='0.8.0',
  description='Search and edit your Markdown reading list',
  long_description=readme,
  author='Alex Claman',
  author_email='claman@alexclaman.com',
  url='https://github.com/claman/percival',
  license='license'
)
