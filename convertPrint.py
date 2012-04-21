from convertToken import convertToken
from convertLineEnd import convertLineEnd

__author__ = 'Alexis Shaw'

import re
import tokenize

__author__ = 'Alexis Shaw'

def convertPrint(token,line, t, v, i,understood,variables):
    """

    """
    line += 'print '

    i += 1
    (t, v, b, _,_) = token[i]
    while t != tokenize.ENDMARKER :
        if t == tokenize.NEWLINE or t == tokenize.ENDMARKER:
            if not (i >= 1 and token[i-1][0] == tokenize.OP and token[i-1][1] == ','):
                line += r'. "\n"'
            return convertLineEnd(token, line,t,v,i,understood,variables)
        elif t == tokenize.OP and re.match(';',v):
            if not (i >= 1 and token[i-1][0] == tokenize.OP and token[i-1][1] == ','):
                line += r'."\n"; '
            else:
                line += v + " "
            return line, i, understood,variables
        else:
            line, i, understood,variables = convertToken(token,line,t,v,i,understood,variables)
        i += 1
        (t, v, b, _,_) = token[i]

    return line, i, understood

