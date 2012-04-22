import tokenize
from getFunctionExpression import getFunctionExpression

__author__ = 'Alexis Shaw'

def convertSys(token, line, t,v,i,understood, variables, oldIdent):
    if token[i+1][0] == tokenize.OP   and token[i+1][1] == '.'      and \
       token[i+2][0] == tokenize.NAME and token[i+2][1] == 'stdout' and\
       token[i+3][0] == tokenize.OP   and token[i+3][1] == '.'      and\
       token[i+4][0] == tokenize.NAME and token[i+4][1] == 'write'  and \
       token[i+5][0] == tokenize.OP   and token[i+5][1] == '(':
        toWrite = ''
        i+= 6
        toWrite, i, understood,variables = getFunctionExpression(token, toWrite,t,v,i,understood,variables, oldIdent)
        line += 'print( '+toWrite + ')'
        i -= 1
    elif token[i+1][0] == tokenize.OP   and token[i+1][1] == '.'      and\
         token[i+2][0] == tokenize.NAME and token[i+2][1] == 'stdin'    and\
         token[i+3][0] == tokenize.OP   and token[i+3][1] == '.'        and\
         token[i+4][0] == tokenize.NAME and token[i+4][1] == 'readline' and\
         token[i+5][0] == tokenize.OP   and token[i+5][1] == '('        and\
         token[i+6][0] == tokenize.OP   and token[i+6][1] == ')':
        line += '<STDIN>'
        i += 6
    elif token[i+1][0] == tokenize.OP   and token[i+1][1] == '.'        and\
         token[i+2][0] == tokenize.NAME and token[i+2][1] == 'stdin'    and\
         token[i+3][0] == tokenize.OP   and token[i+3][1] == '.'        and\
         token[i+4][0] == tokenize.NAME and token[i+4][1] == 'readlines' and\
         token[i+5][0] == tokenize.OP   and token[i+5][1] == '('        and\
         token[i+6][0] == tokenize.OP   and token[i+6][1] == ')':
        line += '<STDIN>'
        i += 6
    elif token[i-1][0] == tokenize.NAME and token[i-1][1] == 'import':
        line += ''
    return line,i,understood,variables
def isReadlines(token, i):
    if token[i][0]   == tokenize.NAME and token[i][1]   == 'sys'      and\
       token[i+1][0] == tokenize.OP   and token[i+1][1] == '.'        and\
       token[i+2][0] == tokenize.NAME and token[i+2][1] == 'stdin'    and\
       token[i+3][0] == tokenize.OP   and token[i+3][1] == '.'        and\
       token[i+4][0] == tokenize.NAME and token[i+4][1] == 'readlines' and\
       token[i+5][0] == tokenize.OP   and token[i+5][1] == '('        and\
       token[i+6][0] == tokenize.OP   and token[i+6][1] == ')':
        return True
    else:
        return False
def isReadline(token, i):
    if token[i][0]   == tokenize.NAME and token[i][1]   == 'sys'      and\
       token[i+1][0] == tokenize.OP   and token[i+1][1] == '.'        and\
       token[i+2][0] == tokenize.NAME and token[i+2][1] == 'stdin'    and\
       token[i+3][0] == tokenize.OP   and token[i+3][1] == '.'        and\
       token[i+4][0] == tokenize.NAME and token[i+4][1] == 'readline' and\
       token[i+5][0] == tokenize.OP   and token[i+5][1] == '('        and\
       token[i+6][0] == tokenize.OP   and token[i+6][1] == ')':
        return True
    else:
        return False
