#!/usr/bin/env python3

import unittest

def trim(nums, a, b):
    res = []
    for i in nums:
        if i < a:
            res.append(a)
        elif i > b:
            res.append(b)
        else:
            res.append(i)
    return res

class TrimTest(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        res = [4, 4, 4, 4, 5, 6, 6, 6, 6, 6]
        self.assertEqual(trim(nums, 4, 6), res)

    def test_2(self):
        nums = [1.01, 2.02, 3.03, 4.04, 5.05, 6.06, 7.07]
        res = [3, 3, 3.03, 4.04, 5.05, 6, 6]
        self.assertEqual(trim(nums, 3, 6), res)

    def test_3(self):
        nums = [0, -56, 165, 82, 9, 77, 11, -98, 15, 103]
        res = [71, 71, 103, 82, 71, 77, 71, 71, 71, 103]
        self.assertEqual(trim(nums, 71, 103), res)

if __name__ == '__main__':
    unittest.main()