import hashlib
import math
import bitarray

from uuid import uuid4


class BloomFilter(object):

    def __init__(self, capacity, error_rate=0.001):
        # n = number of items in the filter, p number of false positives e.g error rate, m number of bits in the
        # filter, k number of hash functions

        # m = ceil((n * log(p)) / log(1 / pow(2, log(2))));
        # k = round((m / n) * log(2));

        self.num_bits = math.ceil((capacity * math.log(error_rate)) / math.log(1 / math.pow(2, math.log(2))))
        self.num_hash_functions = round((self.num_bits / capacity) * math.log(2))
        self.capacity = capacity
        self.error_rate = error_rate
        self.bitarray = bitarray.bitarray(self.num_bits, endian='little')
        self.bitarray.setall(False)

        self.count = 0
        self.salts = self._prep_salts(self.num_hash_functions)

    def _prep_salts(self, num_hash_functions):
        return [uuid4() for i in range(num_hash_functions)]

    def __contains__(self, key):
        for salt in self.salts:
            idx = self._hash_value(key, salt)
            if not self.bitarray[idx]:
                return False
        return True

    def __len__(self):
        return self.count

    def _hash_value(self, key, salt):
        hashfunc = hashlib.sha256()
        if isinstance(key, str):
            key = key.encode('utf-8')
        else:
            key = str(key).encode('utf-8')

        hashfunc.update(key + salt.bytes)
        uint = int.from_bytes(hashfunc.digest(), "little")
        return uint % self.num_bits

    def add(self, key):
        if self.count > self.capacity:
            raise IndexError("BloomFilter is full")

        for salt in self.salts:
            idx = self._hash_value(key, salt)
            self.bitarray[idx] = True

        self.count += 1
