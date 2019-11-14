#!/usr/bin/env python
from setuptools import setup

VERSION = '1.1.0'
DESCRIPTION = "bloomfpy: Bloom Filter implementation for python, a probabilistic data structure"
LONG_DESCRIPTION = """
bloomfpy is a bloom filter implemented in python, bloom filters are probabilistic data structures with sub linear space requirements.
"""

CLASSIFIERS = filter(None, map(str.strip,
"""
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python :: 3.7
Operating System :: OS Independent
Topic :: Utilities
Topic :: Database :: Database Engines/Servers
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))

setup(
    name="bloomfpy",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords=('data structures', 'bloom filter', 'bloom', 'filter',
              'probabilistic', 'set'),
    author="Berkay Dinçer",
    author_email="dincerbberkay@gmail.com",
    url="https://github.com/berkay-dincer/bloompy",
    license="MIT License",
    platforms=['any'],
    zip_safe=True,
    install_requires=['bitarray>=1.1.0'],
    packages=['bloomfpy']
)