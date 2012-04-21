import keyword
from tokenize import generate_tokens
import tokenize

__author__ = 'Alexis Shaw'

import sys
import os
import re

def convertAndPrint(f):
    """
    Converts a python program file into perl program file
    """
    result = ""
    g = generate_tokens(f.readline)
    line = ""
    understood = True
    printStatement = False
    for t, v, b, _,_ in g:
        if t == tokenize.COMMENT:
            if b[0] == 1 and re.match(r'^#!',v):
                line += '#!/usr/bin/perl -w'
            else :
                line += v
                line += ' '
        elif t == tokenize.NAME:
            if keyword.iskeyword(v):
                if v == 'print':
                    line += 'say '
                    printStatement = True
                else:
                    line += v + ' '
                    understood = False
            else:
                line += '$' + v + ' '
        elif t == tokenize.STRING:
            if re.match("^'.*'$", v):
                line += re.sub("^'(.*)'$",'"\1"',v)
            elif re.match("^[r|R](['|\"])(.*)\1$", v):
                line += re.sub("^[r|R](['|\"])(.*)\1$", "'\1'",v)
            else:
                line += v
            line += ' '
        elif t == tokenize.NEWLINE or t == tokenize.NL:
            if understood:
                if printStatement:
                    line += r".'\n'"
                print line
            else:
                print '#'+line
            understood = True
            line = ''
        else:
            line += v + ' '
            understood = False




files = []
if len( sys.argv[1:]) == 0:
    files.append('-')
else:
    files = sys.argv[1:]

for f in files:
    if os.path.isfile(f):
        convertAndPrint(open(f))
    elif f == '-':
        convertAndPrint(sys.stdin)



