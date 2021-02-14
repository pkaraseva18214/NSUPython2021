#!/usr/bin/env python3

def cut_by_range(nums, a, b):
    for i in range(len(nums)):
        if nums[i] < a:
            nums[i] = a
        elif nums[i] > b:
            nums[i] = b
    return nums


input = list(map(int, input().split()))
a = int(input())
b = int(input())
print(cut_by_range(input, a, b))