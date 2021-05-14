#!/usr/bin/env python3

import unittest
from problem2 import reverse_dict

class ReverseTest(unittest.TestCase):

  def test_reverse(self):
    d = {"a": ["b"], "c": ["d"]}
    expected = {"b": set(["a"]), "d": set(["c"])}
    self.assertEqual(reverse_dict(d), expected)

  def test_duplicate_values(self):
    d = {"apple": ["malum", "pomum", "popula", "malum"]}
    expected = {"malum": set(["apple"]), "pomum": set(["apple"]), "popula": set(["apple"])}
    self.assertEqual(reverse_dict(d), expected)

  def test_synonims(self):
    d = {"a": ["b", "c"], "d": ["b", "e"]}
    expected = {"b": set(["a", "d"]), "c": set(["a"]), "e": set(["d"])}
    self.assertEqual(reverse_dict(d), expected)

if __name__ == "__main__":
  unittest.main()
