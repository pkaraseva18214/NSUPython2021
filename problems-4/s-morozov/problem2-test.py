#!/usr/bin/env python3

import unittest
from problem2 import translate

class TranslateTest(unittest.TestCase):
  def test_replace(self):
    self.assertEqual(translate("abracadabra", "ab", "cd"), "cdrcccdcdrc")

  def test_delete(self):
    self.assertEqual(translate("abracadabra", "", "", "ar"), "bcdb")

  def test_replace_delete(self):
    self.assertEqual(translate("abracadabra", "ab", "cd", "r"), "cdcccdcdc")

  def test_replace_delete_overlap(self):
    self.assertEqual(translate("abracadabra", "ab", "cd", "a"), "drcddr")

  def test_illegal_replacement_count(self):
    self.assertRaises(ValueError, translate, "abracadabra", "ab", "cde")

  def test_duplicate_replacement(self):
    self.assertRaises(ValueError, translate, "abracadabra", "aba", "cde")

if __name__ == "__main__":
  unittest.main()
