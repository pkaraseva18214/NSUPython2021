#!/usr/bin/env python3

def cusum(numbers):
    res = []
    csum = 0
    for num in numbers:
        csum += num
        res.append(csum)
    return res


if __name__ == '__main__':
    print(cusum(map(int, input().split(' '))))
