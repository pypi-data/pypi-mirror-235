from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='peopleprinter',
  version='0.0.1',
  author='forsunkin',
  author_email='guazah@gmail.com',
  description='This is the simplest module for parsing printers in local network.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Forsunkin/PeoplePrinter',
  packages=find_packages(),
  install_requires=['requests', 'bs4', ],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='printer parsing',
  project_urls={
    'GitHub': 'https://github.com/Forsunkin/PeoplePrinter'
  },
  python_requires='>=3.6'
)