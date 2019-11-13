# bloomfpy
A probabilistic data structure called Bloom Filter implemented in python. 

Bloom Filters are very efficient data structures built for set membership problems. They take sublinear memory space with O(k) complexity for inserting and checking membership.

This implementation calculates the `k` (# of hash functions) and `m` (# of bits) from a given `m` (capacity) and `p` (error_rate):

- m = ceil((n * log(p)) / log(1 / pow(2, log(2))))
- k = round((m / n) * log(2))

# Usage: 

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
# Installation:

bloomfpy is available via pypi:

run `pip install bloomfpy`
