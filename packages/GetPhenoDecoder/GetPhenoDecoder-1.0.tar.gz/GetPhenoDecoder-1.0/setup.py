from setuptools import setup, find_packages
setup(
  name='GetPhenoDecoder',
  version='1.0',
  description='A package for landscape-scale phenology extraction using vegetation index time series!',
  author='Rubisco Ren',
  author_email='rubisco51999@gmail.com',
  packages=find_packages(),
  install_requires=[
    'numpy',
    'scipy',
    'matplotlib'
  ],
)