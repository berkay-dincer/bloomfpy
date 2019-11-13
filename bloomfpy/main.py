from bloomfpy import BloomFilter
from uuid import uuid4

g = BloomFilter(capacity=100)

for i in range(0, 99):
    g.add(str(uuid4()))




print('asdasd' in g)