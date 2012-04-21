#!/usr/bin/env python
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
    token = []
    for l in g:
        token.append(l)
    line = ""
    understood = True
    printStatement = False
    variables = {}
    for i, (t, v, b, _,_) in enumerate(token):
        if t == tokenize.COMMENT:
            if b[0] == 1 and re.match(r'^#!',v):
                line += '#!/usr/bin/perl -w'
            elif token[i + 1][0] == tokenize.NEWLINE :
                line += ';' + v
            else:
                line += v
        elif t == tokenize.NAME:
            if keyword.iskeyword(v):
                if v == 'print':
                    line += 'print '
                    printStatement = True
                else:
                    line += v + ' '
                    understood = False
            else:
                line += '$' + v + ' '
                variables[v] = v
        elif t == tokenize.STRING:
            if re.match("^'(.*)'$", v):
                string = re.sub(r"^'(.*)'$",'"\\1"',v)
            elif re.match("^[r|R](['|\"])(.*)\1$", v):
                string = re.sub("^[r|R](['|\"])(.*)\1$", "'\\1'",v)
            else:
                string = v

            line += string + ' '
            if token[i+1][0] == tokenize.COMMENT and \
               token[i+2][0] == tokenize.NL and \
               token[i+3][0] == tokenize.STRING:
                line += '. '
            elif token[i+1][0] == tokenize.NL and\
                token[i+2][0]  == tokenize.STRING:
                line += '. '
            elif token[i+1][0] == tokenize.STRING:
                line += '. '

        elif t == tokenize.NEWLINE or t == tokenize.NL:
            if t == tokenize.NEWLINE and printStatement:
                printStatement = False
                if not (i >= 1 and token[i-1][0] == tokenize.OP and token[i-1][1] == ','):
                    line += r'. "\n"'
            if t == tokenize.NEWLINE and i >= 1 and token[i-1][0] != tokenize.COMMENT:
                line += ';'
            if understood:
                print line
            else:
                print '#'+line
            understood = True
            line = ''
        elif t == tokenize.NUMBER:
            line += v + ' '
        elif t == tokenize.OP and re.match(r'[=+*%,-]',v):
            line += v + ' '
        elif t == tokenize.OP and re.match(';',v):
            printStatement = False
            if not (i >= 1 and token[i-1][0] == tokenize.OP and token[i-1][1] == ','):
                line += r'."\n"'
        else:
            line += v + ' ' + tokenize.tok_name[t]
            understood = False
    print line,




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



