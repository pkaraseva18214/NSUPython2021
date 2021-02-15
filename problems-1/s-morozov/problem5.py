#!/usr/bin/env python3

def factorize(n):
  res = []
  p = 0
  while n % 2 == 0:
    p += 1
    n /= 2
  if p != 0:
    res.append([2, p])
  i = 3
  while n > 1:
    p = 0
    while n % i == 0:
      n //= i
      p += 1
    if p != 0:
      res.append([i, p])
    i += 2
  return res

n = int(input())
print(factorize(n))
