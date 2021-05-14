#!/usr/bin/env python3

import sys
from argparse import ArgumentParser

def reverse_dict(dictionary):
  res = {}
  for word in dictionary:
    for translation in dictionary[word]:
      if translation in res:
        res[translation].add(word)
      else:
        res[translation] = set([word])
  return res

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("filename", help="Name of file with dictionary")
  args = parser.parse_args()

  try:
    with open(args.filename, "r") as file:
      dictionary = {}
      for line in file:
        word, translations = line.rstrip().split(" - ")
        if word in dictionary:
          print(f"Duplicate entry in dictionary: {word}", file=sys.stderr)
          exit()
        dictionary[word] = translations.split(", ")
      res = reverse_dict(dictionary)
      for word, translations in sorted(res.items()):
        print(f"{word} - {', '.join(sorted(translations))}")
  except IOError as e:
    print(f"Unable to open file: {str(e)}", file=sys.stderr)
