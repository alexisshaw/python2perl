#!/usr/bin/python
import sys

__author__ = 'Alexis Shaw'

array = []

for l in sys.stdin.readlines(): array.append(l)

while len(array) > 0:
    print array.pop()

