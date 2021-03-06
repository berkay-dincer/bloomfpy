# (scalable) bloomfpy
A probabilistic data structure called Bloom Filter implemented in python with scaling capabilities. 

Bloom Filters are very efficient data structures built for set membership problems. They take sublinear memory space with O(k) complexity for inserting and checking membership.

This implementation calculates the `k` (# of hash functions) and `m` (# of bits) from a given `n` (capacity) and `p` (error_rate):

- m = ceil((n * log(p)) / log(1 / pow(2, log(2))))
- k = round((m / n) * log(2))

# Usage: 

For a non-scalable bloom filter:

```
>>> from bloomfpy import BloomFilter

>>> f = BloomFilter(capacity=10000, error_rate=0.001)

>>> f.add("100")

>>> print("1" in f)
False
>>> print("100" in f)
True
>>> print(len(f))
1

```

For a scalable floom filter:

```
>>> from bloomfpy import ScalableBloomFilter

>>> s = ScalableBloomFilter(capacity=5, scale_at=0.5) # scale this bloom filter when it is half full

>>> s.add(1)
>>> s.add(2)
>>> s.add(3) # at this point BloomFilter is scaled

>>> print(1 in s)
True

>>> print(3 in s)
True

>>> print(100 in s)
False

```

# Choosing Parameters:

Use the following website to choose and understand the consequences of picking faulty parameters.

https://hur.st/bloomfilter/?n=120000&p=1.0E-5&m=&k=

# Installation:

bloomfpy is available via pypi:

run `pip install bloomfpy`
