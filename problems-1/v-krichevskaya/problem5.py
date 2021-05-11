#!/usr/bin/env python3

import unittest

def prime_nums(n):
    res = []
    for i in range(2, int((n ** 0.5) + 1)):
        st = 0
        while n % i == 0:
            st += 1
            n /= i
        if st != 0:
            res.append([i, st])
        if n == 1:
            break
    return res if len(res) > 0 else [[n, 1]]


class PrimeNumbersTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(prime_nums(12), [[2, 2], [3, 1]])

    def test_2(self):
        self.assertEqual(prime_nums(360), [[2, 3], [3, 2], [5, 1]])

    def test_3(self):
        self.assertEqual(prime_nums(144), [[2, 4], [3, 2]])

    def test_4(self):
        self.assertEqual(prime_nums(5), [[5, 1]])

if __name__ == '__main__':
    unittest.main()