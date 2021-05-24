#!/usr/bin/env python3

import unittest
from problem1 import get_triples

class TriplesTest(unittest.TestCase):
  def test_negative(self):
    self.assertEqual(get_triples(-10), [])

  def test_zero(self):
    self.assertEqual(get_triples(0), [])

  # Assert that the triple containing a number equal to n is included
  def test_equal(self):
    self.assertEqual(get_triples(5), [(3, 4, 5)])

  # Assert that the triple containing numbers less than n is included
  def test_less(self):
    self.assertEqual(get_triples(6), [(3, 4, 5)])

  def test_multiple(self):
    self.assertEqual(get_triples(11), [(3, 4, 5), (6, 8, 10)])

if __name__ == "__main__":
  unittest.main()

