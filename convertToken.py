import keyword
import re
import tokenize
from convertComment import convertComment
from convertElif import convertElif
from convertElse import convertElse
from convertFor import convertFor
from convertGrouping import convertGrouping
from convertIf import convertIf
from convertInt import convertInt
from convertLineEnd import convertLineEnd
from convertNot import convertNot
from convertPrint import convertPrint
from convertRange import convertRange
from convertString import convertString
from convertSys import convertSys
from convertWhile import convertWhile

__author__ = 'Alexis Shaw'
def convertToken(token, line,t,v,i,understood,variables):
    """
    Converts a token in Python into an equivelent Perl string
    """
    if t == tokenize.COMMENT: line,i,understood,variables = convertComment(token,line,t,v,i,understood,variables)
    elif t == tokenize.NAME:
        if keyword.iskeyword(v):
            if   v == 'print': line, i, understood, variables = convertPrint(token,line,t,v,i,understood,variables)
            elif v == 'not'  : line, i, understood, variables = convertNot  (token,line,t,v,i,understood,variables)
            elif v == 'and'  : line += '&& '
            elif v == 'or'   : line += '|| '
            elif v == 'if'   : line, i, understood, variables = convertIf   (token,line,t,v,i,understood,variables)
            elif v == 'for'  : line, i, understood, variables = convertFor  (token,line,t,v,i,understood,variables)
            elif v == 'while': line, i, understood, variables = convertWhile(token,line,t,v,i,understood,variables)
            elif v == 'elif' : line, i, understood, variables = convertElif (token,line,t,v,i,understood,variables)
            elif v == 'else' : line, i, understood, variables = convertElse (token,line,t,v,i,understood,variables)
            elif v == 'break': line += 'last '
            elif v == 'continue': line += 'next'
            else:
                line += v + ' '
                understood = False
        elif v == 'range': line, i, understood, variables = convertRange(token, line, t,v,i,understood, variables)
        elif v == 'sys'  : line, i, understood, variables = convertSys  (token, line, t,v,i,understood, variables)
        elif v == 'int'  : line, i, understood, variables = convertInt  (token, line, t,v,i,understood, variables)
        else: line += '$' + v + ' '
    elif t == tokenize.STRING: line,i = convertString(token,line, t, v, i)
    elif t == tokenize.NEWLINE: line, i,understood,variables = convertLineEnd(token,line,t,v,i,understood,variables);
    elif t == tokenize.NL: line, i,understood,variables = convertLineEnd(token,line,t,v,i,understood,variables);
    elif t == tokenize.NUMBER:line += v + ' '
    elif t == tokenize.OP and re.match(r'^[<>&^|~=+*%,-]$|^\*\*$|<<|>>|>=|<=|!=|==|\+=|-=|\*=|%=|&=',v): line += v + ' '
    elif t == tokenize.OP and re.match('[(]',v): line, i,understood,variables = convertGrouping(token,line,t,v,i,understood,variables)
    elif t == tokenize.ENDMARKER: print "",
    else:
        line += v + ' '
        understood = False
    return line,i,understood,variables
