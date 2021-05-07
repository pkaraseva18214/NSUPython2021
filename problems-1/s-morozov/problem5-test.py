#!/usr/bin/env python3

import unittest
from problem5 import factorize

class FactorizeTest(unittest.TestCase):
  def test_prime(self):
    self.assertEqual(factorize(37), [[37, 1]])

  def test_composite(self):
    self.assertEqual(factorize(12), [[2, 2], [3, 1]])

  def test_one(self):
    self.assertEqual(factorize(1), [])

  def test_negative(self):
    self.assertEqual(factorize(-5), [])

if __name__ == '__main__':
  unittest.main()

