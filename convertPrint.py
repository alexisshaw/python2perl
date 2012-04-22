import convertToken

__author__ = 'Alexis Shaw'

import re
import tokenize

def convertPrint(token,line, t, v, i,understood,variables):
    """

    """
    line += 'print '

    i += 1
    (t, v, _, _,_) = token[i]
    while len(token)-i > 0 :
        (t, v, _, _,_) = token[i]
        if t == tokenize.NEWLINE or t == tokenize.ENDMARKER:
            break
        elif t == tokenize.OP and re.match(';',v):
            break
        elif t == tokenize.OP and v == ',':
            if token[i+1][0] == tokenize.NEWLINE or token[i+1][0] == tokenize.ENDMARKER:
                line = line
            elif token[i+1][0] == tokenize.OP and token[i+1][1] == ';':
                line = line
            else:
                line, i, understood,variables = convertToken.convertToken(token,line,t,v,i,understood,variables)
        else:
            line, i, understood,variables = convertToken.convertToken(token,line,t,v,i,understood,variables)
        i += 1
    if not (i >= 1 and token[i-1][0] == tokenize.OP and token[i-1][1] == ','):
            line += r'. "\n"'
    i -= 1
    return line, i, understood,variables


