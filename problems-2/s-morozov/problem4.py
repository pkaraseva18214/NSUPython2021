#!/usr/bin/env python3

import sys

def find_in_pi(seq, pi):
  pos_cnt = 0
  positions = []
  start_pos = pi.find('.', 0) + 1
  cur_pos = pi.find(seq, start_pos)

  while cur_pos != -1:
    pos_cnt += 1
    if (pos_cnt <= 5):
      positions.append(cur_pos - start_pos)
    cur_pos = pi.find(seq, cur_pos + 1)

  return pos_cnt, positions

if __name__ == '__main__':
  if len(sys.argv) == 1:
    seq = input('Enter sequence to search for.\n')
  else:
    seq = sys.argv[1]
  try:
    with open('pi.txt', 'r') as file:
      pi = file.read().replace('\n', '')
    pos_cnt, positions = find_in_pi(seq, pi)
    print(f'Found {pos_cnt} results.\nPositions: {" ".join(map(str, positions))} ...')
  except IOError as e:
    print(f'Unable to open file: {str(e)}', file = sys.stderr)
