import convertLineEnd
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
            if not (i >= 1 and token[i-1][0] == tokenize.OP and token[i-1][1] == ','):
                line += r'. "\n"'
            return convertLineEnd.convertLineEnd(token, line,t,v,i,understood,variables)
        elif t == tokenize.OP and re.match(';',v):
            if not (i >= 1 and token[i-1][0] == tokenize.OP and token[i-1][1] == ','):
                line += r'."\n"; '
            else:
                line += v + " "
            return line, i, understood,variables
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
    return convertLineEnd.convertLineEnd(token, line,t,v,i,understood,variables)


