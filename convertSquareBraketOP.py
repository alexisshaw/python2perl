import re
import tokenize
import convertListLiteral
import convertSliceOperator

__author__ = 'Alexis Shaw'

def convertSquareBraketOP(token,line,t,v,i,understood,variables):
    if re.match('[=([]', token[i-1][1]) or token[i-1][0] == tokenize.NEWLINE:
        return convertListLiteral.convertListLiteral(token,line,t,v,i,understood,variables)
    else:
        token, line, understood,variables,_= convertSliceOperator.convertSliceOperator(token,line,t,v,i,understood,variables)
        return token,line,understood,variables

