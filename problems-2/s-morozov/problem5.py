#!/usr/bin/env python3

import math

def get_primes(n):
  return [x for x in range (2, n + 1) if not any(x % y == 0 for y in range(2, int(math.sqrt(x)) + 1))]

if __name__ == '__main__':
  try:
    n = int(input())
    print(get_primes(n))
  except ValueError:
    print("Illegal input")
