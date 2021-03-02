#!/usr/bin/env python3

try:
    path = input('Enter path to file.\n')
    inp = input('Enter sequence to search for.\n')
    occurrences = []

    with open(path, 'r') as file:
        text = ''.join(file.read().split())

    result = str.find(text, inp)
    while result != -1:
        occurrences.append(result - 2)
        result = str.find(text, inp, result + 1)

    oc_len = len(occurrences)
    print('Found {n} results.\nPositions: {p}'.format(n=oc_len,
                                                      p=' '.join([str(value) for value in occurrences[:5]]) + ' ...'
                                                      if oc_len > 0 else 'No positions'))
except FileNotFoundError:
    print('Can not find file with given path.')
