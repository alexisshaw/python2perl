import keyword
import re
import tokenize
from convertLineEnd import convertLineEnd
from convertNot import convertNot
from convertPrint import convertPrint
from convertString import convertString

__author__ = 'Alexis Shaw'
def convertToken(token, line,t,v,i,understood,variables):
    """
    Converts a token in Python into an equivelent Perl string
    """
    #print tokenize.tok_name[t],' ',
    if t == tokenize.COMMENT:
        if i == 0 and re.match(r'^#!',v):
            line += '#!/usr/bin/perl -w'
        elif token[i + 1][0] == tokenize.NEWLINE :
            line += ';' + v
        else:
            line += v
    elif t == tokenize.NAME:
        if keyword.iskeyword(v):
            if   v == 'print': line, i, understood, variables = convertPrint(token,line,t,v,i,understood,variables)
            elif v == 'not'  : line, i, understood, variables = convertNot(token,line,t,v,i,understood,variables)
            elif v == 'and'  : line += '&& '
            elif v == 'or'   : line += '|| '
            elif v == 'if'   : line, i, understood, variables = convertIf(token,line,t,v,i,understood,variables)
            elif v == 'for'  : line, i, understood, variables = convertFor(token,line,t,v,i,understood,variables)
            elif v == 'while': line, i, understood, variables = convertWhile(token,line,t,v,i,understood,variables)
            else:
                line += v + ' '
                understood = False
        else:
            line += '$' + v + ' '
            variables[v] = v

    elif t == tokenize.STRING:
        line,i = convertString(token,line, t, v, i)

    elif t == tokenize.NEWLINE or t == tokenize.ENDMARKER or t == tokenize.NL:
        line, i,understood,variables = convertLineEnd(token,line,t,v,i,understood,variables)
    elif t == tokenize.NUMBER:
        line += v + ' '
    elif t == tokenize.OP and re.match(r'^[<>&^|~=+*%,-]$|^\*\*$|<<|>>|>=|<=|!=|==',v):
        line += v + ' '
    else:
        line += v + ' '
        understood = False
    return line,i,understood,variables
