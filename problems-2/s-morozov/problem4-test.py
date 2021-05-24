#!/usr/bin/env python3

import unittest
from problem4 import find_in_pi

class PiTest(unittest.TestCase):

  def test_empty(self):
    self.assertEqual(find_in_pi('', '3.1415926'), (8, [0, 1, 2, 3, 4]))

  def test_wrong_seq(self):
    self.assertEqual(find_in_pi('qwerty', '3.1415926'), (0, []))

  def test_less_than_5(self):
    self.assertEqual(find_in_pi('1828', '2.718281828459'), (2, [1, 5]))

  def test_real_pi(self):
    with open('pi.txt') as file:
      pi = file.read().replace('\n', '')
    self.assertEqual(find_in_pi('123', pi), (4185, [1923, 2937, 2975, 3891, 6547]))


if __name__ == '__main__':
  unittest.main()
