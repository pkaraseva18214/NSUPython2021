#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
  seq = input('Enter sequence to search for.\n')
else:
  seq = sys.argv[1]


with open('pi.txt', 'r') as file:
  pi = file.read().replace('\n', '')

pos_cnt = 0
positions = []

start_pos = 2
cur_pos = pi.find(seq, start_pos)

while cur_pos != -1:
  pos_cnt += 1
  if (pos_cnt <= 5):
    positions.append(cur_pos - start_pos)
  cur_pos = pi.find(seq, cur_pos + 1)

print(f'Found {pos_cnt} results.\nPositions: {" ".join(map(str, positions))} ...')

