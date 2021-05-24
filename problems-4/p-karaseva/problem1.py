#!/usr/bin/env python3

import argparse
import csv
from problem1 import Table


def get_head(args):
    t = Table()
    with open(args.file) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=";")
        for line in tsvreader:
            t.add_row(line)
    print(t.head(args.n))


def get_tail(args):
    t = Table()
    with open(args.file) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=";")
        for line in tsvreader:
            t.add_row(line)
    print(t.tail(args.n))


def paste(args):
    t1 = Table()
    with open(args.file_first) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=";")
        for line in tsvreader:
            t1.add_row(line)
    t2 = Table()
    with open(args.file_second) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=";")
        for line in tsvreader:
            t2.add_row(line)
    print(t1.merge_by_columns(t2))


def cut(args):
    t = Table()
    with open(args.file) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=";")
        for line in tsvreader:
            t.add_row(line)

    f = args.f.replace("'", "")
    f = f.split(',')
    indexes = []
    for s in f:
        indexes.append(int(s))
    print(t.get_columns(indexes))


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_head = subparsers.add_parser('head')
parser_head.add_argument('-n', type=int, default=1)
parser_head.add_argument('file', help='file')
parser_head.set_defaults(func=get_head)

parser_tail = subparsers.add_parser('tail')
parser_tail.add_argument('-n', type=int, default=1)
parser_tail.add_argument('file', help='file')
parser_tail.set_defaults(func=get_tail)

parser_tail = subparsers.add_parser('paste')
parser_tail.add_argument('-file_first', help='file with first table')
parser_tail.add_argument('file_second', help='file with second table')
parser_tail.set_defaults(func=paste)

parser_tail = subparsers.add_parser('cut')
parser_tail.add_argument('-f', type=ascii, help='indexes')
parser_tail.add_argument('file', help='file with second table')
parser_tail.set_defaults(func=cut)

if __name__ == "__main__":
    print("Cut")
    args4 = parser.parse_args('cut -f 0,1,1 t1.tsv'.split())
    args4.func(args4)
    args = parser.parse_args('head -n 2 t1.tsv'.split())
    args2 = parser.parse_args('tail -n 1 t1.tsv'.split())
    args3 = parser.parse_args('paste -file_first t1.tsv t.tsv'.split())
    print("Head")
    args.func(args)
    print("Tail")
    args2.func(args2)
    print("Paste")
    args3.func(args3)

