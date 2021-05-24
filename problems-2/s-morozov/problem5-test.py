#!/usr/bin/env python3

import unittest
from problem5 import get_primes

class PrimeTest(unittest.TestCase):
  def test_negative(self):
    self.assertEqual(get_primes(-5), [])

  def test_zero(self):
    self.assertEqual(get_primes(0), [])

  def test_one(self):
    self.assertEqual(get_primes(1), [])

  def test_two(self):
    self.assertEqual(get_primes(2), [2])

  def test_prime(self):
    self.assertEqual(get_primes(17), [2, 3, 5, 7, 11, 13, 17])

  def test_composite(self):
    self.assertEqual(get_primes(18), [2, 3, 5, 7, 11, 13, 17])

if __name__ == "__main__":
  unittest.main()
