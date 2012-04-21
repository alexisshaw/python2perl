import re
import tokenize

__author__ = 'Alexis Shaw'

def convertString(token,line, t, v, i):
    if re.match("^'(.*)'$", v):
        string = re.sub(r"^'(.*)'$",'"\\1"',v)
    elif re.match("^[r|R](['|\"])(.*)\1$", v):
        string = re.sub("^[r|R](['|\"])(.*)\1$", "'\\1'",v)
    else:
        string = v

    line += string + ' '
    if token[i+1][0] == tokenize.COMMENT and\
       token[i+2][0] == tokenize.NL and\
       token[i+3][0] == tokenize.STRING:
        line += '. '
    elif token[i+1][0] == tokenize.NL and\
         token[i+2][0]  == tokenize.STRING:
        line += '. '
    elif token[i+1][0] == tokenize.STRING:
        line += '. '
    return line, i
