#!/usr/bin/env python3

import unittest

def cumsum(nums):
    res = [0]
    for elem in nums:
        res.append(res[-1] + elem)
    return res

class CumSumTest(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3]
        res = [0, 1, 3, 6]
        self.assertEqual(cumsum(nums), res)

    def test_2(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        res = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        self.assertEqual(cumsum(nums), res)

    def test_3(self):
        nums = [0, -56, 165, 82, 9, 77, 11, -98, 15, 103]
        res = [0, 0, -56, 109, 191, 200, 277, 288, 190, 205, 308]
        self.assertEqual(cumsum(nums), res)


if __name__ == '__main__':
    unittest.main()