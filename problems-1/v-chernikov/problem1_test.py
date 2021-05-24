#!/usr/bin/env python3

import unittest
from problem1 import cusum


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(cusum([]), [0])

    def test_single(self):
        self.assertEqual(cusum([100]), [0, 100])

    def test_ones(self):
        self.assertEqual(cusum([1, 1, 1, 1, 1]), [0, 1, 2, 3, 4, 5])

    def test_twos(self):
        self.assertEqual(cusum([2, 2, 2, 2, 2]), [0, 2, 4, 6, 8, 10])

    def test_to_five(self):
        self.assertEqual(cusum([1, 2, 3, 4, 5]), [0, 1, 3, 6, 10, 15])


if __name__ == '__main__':
    unittest.main()
