#!/usr/bin/env python3

from argparse import ArgumentParser
import sys

def translate(string, old_chars, new_chars, delete=""):
  if len(old_chars) != len(new_chars):
    raise ValueError("Old chars count is not equal to new chars count")

  for ch in old_chars:
    if old_chars.count(ch) != 1:
      raise ValueError("Old chars include duplicate characters")

  replacement = dict(zip(old_chars, new_chars))

  return "".join(replacement[ch] if ch in replacement else ch for ch in string if ch not in delete)

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("filename", help="Path to file")
  parser.add_argument("old_chars", help="Characters to be translated")
  parser.add_argument("new_chars", help="Characters to be put instead of replaced characters")
  parser.add_argument("-d", "--delete", help="Characters to be deleted")
  args = parser.parse_args()

  try:
    with open(args.filename, "r") as file:
      content = file.read()
    print(translate(content, args.old_chars, args.new_chars, args.delete if args.delete else ""))
  except ValueError as e:
    print(f"Incorrect input: {str(e)}", file=sys.stderr)
  except IOError as e:
    print(f"Unable to open file: {str(e)}", file=sys.stderr)
