import re
import tokenize

__author__ = 'Alexis Shaw'

def convertComment(token,line,t,v,i,understood,variables):
    if i == 0 and re.match(r'^#!',v): line += '#!/usr/bin/perl -w'
    elif token[i + 1][0] == tokenize.NEWLINE : line += ';' + v
    else: line += v
    return line, i, understood, variables
