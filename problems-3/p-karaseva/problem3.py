#!/usr/bin/env python3
import itertools
import math

class Vector:

    def __init__(self, *args):
        self.values = []
        self.count = len(args)
        for x in args:
            self.values.append(x)

    def __str__(self):
        s = '('
        count = 0
        for x in self.values:
            count += 1
            if count < self.count:
                s += str(x) + ', '
            else:
                s += str(x) + ')'
        return s

    def length(self):
        l = 0
        for x in self.values:
            l += x ** 2
        return math.sqrt(l)

    def multiply_by_scalar(self, num):
        added = list()
        for n in self.values:
            added.append(n * num)
        self.values = added
        return self.values

    def get_element(self, index):
        return self.values[index]

    def equals(self, v2):
        if self.values == v2.values:
            return True
        return False

    def sum(self, v2):
        k = 0
        while k < self.count:
            self.values[k] += v2.values[k]
            k += 1
        return self.values

    def subtract(self, v2):
        k = 0
        while k < self.count:
            self.values[k] -= v2.values[k]
            k += 1
        return self.values

    def scalar_product(self, v2):
        k = 0
        res = 0
        while k < self.count:
            res += self.values[k] * v2.values[k]
            k += 1
        return res

