#!/usr/bin/env python3
from functools import reduce


def cusum(numbers):
    return reduce(lambda csum, x: csum.append(csum[len(csum) - 1] + x) or csum, numbers, [0])


if __name__ == '__main__':
    try:
        print(cusum(map(int, input().split(' '))))
    except ValueError:
        print("Illegal input, try sequence of integers separated with spaces")

