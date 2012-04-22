from convertGrouping import convertGrouping
from convertVariableName import getType

__author__ = 'Alexis Shaw'

def convertLen(token, line, t,v,i,understood, variables):
    type = getType(token, i+1, understood, variables)

    i+= 1
    t,v,_,_,_ = token[i]
    temp, i, understood, variables = convertGrouping(token,line,t,v,i,understood,variables)
    if type == 'LIST':
        line += 'scalar ' + temp
    else:
        line += 'length ' + temp
    return line, i, understood, variables
