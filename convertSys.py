import tokenize
from getFunctionExpression import getFunctionExpression

__author__ = 'Alexis Shaw'

def convertSys(token, line, t,v,i,understood, variables):
    if token[i+1][0] == tokenize.OP   and token[i+1][1] == '.'      and \
       token[i+2][0] == tokenize.NAME and token[i+2][1] == 'stdout' and\
       token[i+3][0] == tokenize.OP   and token[i+3][1] == '.'      and\
       token[i+4][0] == tokenize.NAME and token[i+4][1] == 'write'  and \
       token[i+5][0] == tokenize.OP   and token[i+5][1] == '(':
        toWrite = ''
        i+= 5
        toWrite, i, understood,variables = getFunctionExpression(toWrite, line,t,v,i,understood,variables)
        line += 'print ( ' + toWrite + ')'
    elif token[i+1][0] == tokenize.OP   and token[i+1][1] == '.'        and\
       token[i+2][0] == tokenize.NAME and token[i+2][1] == 'stdin'    and\
       token[i+3][0] == tokenize.OP   and token[i+3][1] == '.'        and\
       token[i+4][0] == tokenize.NAME and token[i+4][1] == 'readline' and\
       token[i+5][0] == tokenize.OP   and token[i+5][1] == '('        and\
       token[i+6][0] == tokenize.OP   and token[i+6][1] == ')':
        line += '<STDIN>'
        i += 6
    return line,i,understood,variables
