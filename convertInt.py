import tokenize
from convertGrouping import convertGrouping

__author__ = 'Alexis Shaw'

def convertInt(token, line, t,v,i,understood, variables):
     if token[i+1][0] == tokenize.OP   and token[i+1][1] == '(':
         toConvert= ''
         toConvert, i, understood,variables = convertGrouping(token,toConvert,t,v,i+1,understood,variables)
         line += '(sprintf ("%d", ' + toConvert + ') + 1 - 1)'
     return line,i,understood,variables
