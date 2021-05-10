#!/usr/bin/env python3

def print_song():
    nums = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'No']

    line = ' green bottle{s} hanging on the wall,'
    st_line = '{} one green bottle should accidentally fall{}'
    end_line = ' green bottle{} hanging on the wall.'

    for i in range(10):
        print(nums[i] + line.format(s='s' if i != 9 else ''))
        print(nums[i] + line.format(s='s' if i != 9 else ''))
        print(st_line.format('And if' if i != 9 else 'If that', ','  if i != 9 else ''))
        print("There'll be " + nums[i + 1].lower() + end_line.format('s' if i != 9 else ''))


if __name__ == '__main__':
    print_song()