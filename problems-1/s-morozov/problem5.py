#!/usr/bin/env python3

def factorize(n):
  res = []
  p = 0
  i = 2
  while n > 1:
    p = 0
    while n % i == 0:
      n //= i
      p += 1
    if p != 0:
      res.append([i, p])
    i += 1
  return res

if __name__ == '__main__':
  n = int(input())
  print(factorize(n))
