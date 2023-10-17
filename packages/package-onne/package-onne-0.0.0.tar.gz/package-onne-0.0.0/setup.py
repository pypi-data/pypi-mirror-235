from setuptools import setup, find_packages

classifiers = [
    "Topic :: Internet",
    "Programming Language :: Python",
]

setup(
  name='package-onne',
  description='Test package',
  long_description=open('README.md').read(),
  url='https://github.com/iPhosgen/package-one',
  author='Your Name',
  author_email='you@example.com',
  license='MIT',
  classifiers=classifiers,
  packages=find_packages(),
  install_requires=['']
)