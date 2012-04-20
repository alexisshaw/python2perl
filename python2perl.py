from convertAndPrint import convertAndPrint

__author__ = 'Alexis Shaw'

import sys
import os

files = []
if not(len( sys.argv[1:]) == 0):
    files[0] = '-'
else:
    files = sys.argv[1:]

for f in files:
    if os.path.exists(f):
        convertAndPrint(open(f).readlines())




