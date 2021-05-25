#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file_to_replace_chars", help="file to replace the characters in")
parser.add_argument("file_result", help="file to write the result")
parser.add_argument("replaced_symbols", help="symbols to be replaced with the new ones")
parser.add_argument("new_symbols", help="symbols to replace with")
parser.add_argument("-d", "--delete", help="symbols to delete")
args = parser.parse_args()

if len(args.replaced_symbols) != len(args.new_symbols):
    raise ValueError('The number of replaced_symbols and new_symbols does not match.')

replaced_symbols_unique = list()
for symbol in args.replaced_symbols:
    if symbol in replaced_symbols_unique:
        raise ValueError('Symbols to be replaced must be different.')
    else:
        replaced_symbols_unique.append(symbol)


try:
    with open(args.file_to_replace_chars, 'r', encoding='utf8') as file_source:
        try:
            with open(args.file_result, 'w', encoding='utf8') as file_res:

                if args.delete:
                    delete_symbols = list(args.delete)
                else:
                    delete_symbols = ()

                table = dict(zip(args.replaced_symbols, args.new_symbols))

                while True:
                    symbol = file_source.read(1)

                    if not symbol:
                        break

                    if symbol in delete_symbols:
                        continue

                    if symbol in table:
                        symbol = table[symbol]

                    file_res.write(symbol)
        except OSError as e:
            sys.stderr.write("Cannot open file to write the result. Check if this file exists or name of the file is "
                             "right.\n")
            sys.stderr.write(str(e))
        finally:
            file_res.close()
except OSError as e:
    sys.stderr.write("Cannot open file with input data. Check if this file exists or name of the file is right.\n")
    sys.stderr.write(str(e))
finally:
    file_source.close()

