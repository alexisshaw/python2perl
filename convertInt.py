import tokenize
from getFunctionExpression import getFunctionExpression

__author__ = 'Alexis Shaw'

def convertInt(token, line, t,v,i,understood, variables):
     if token[i+1][0] == tokenize.OP   and token[i+1][1] == '(':
         i+= 1
         toConvert= ''
         toConvert, i, understood,variables = getFunctionExpression(toConvert, line,t,v,i,understood,variables)
         line += '(sprintf ("%d", ' + toConvert + ') + 1 - 1)'
     return line,i,understood,variables
