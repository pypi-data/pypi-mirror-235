from setuptools import setup, find_packages

setup(name='guardian_exchange',
      packages=find_packages(),
      install_requires=[
          "temporalio"
      ])
