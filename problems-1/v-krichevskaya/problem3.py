#!/usr/bin/env python3

import unittest

def collatz(num):
    res = [num]
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        
        res.append(int(num))
    return res

def collatz_list(num):
    return ' -> '.join(str(x) for x in collatz(num))

class CollatzTest(unittest.TestCase):
    def test_1(self):
        res = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(collatz(7), res)

    def test_2(self):
        res = [2, 1]
        self.assertEqual(collatz(2), res)

    def test_3(self):
        res = '3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1'
        self.assertEqual(collatz_list(3), res)

if __name__ == '__main__':
    unittest.main()