#!/usr/bin/env python3

def get_triples(n):
  return [(x, y, z) for x in range(1, n) for y in range(x + 1, n) for z in range(y + 1, n + 1) if x ** 2 + y ** 2 == z ** 2]

if __name__ == "__main__":
  try:
    n = int(input())
    print(get_triples(n))
  except ValueError:
    print(f"Illegal input")
