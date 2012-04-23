from convertGrouping import convertGrouping
from convertVariableName import getType

__author__ = 'Alexis Shaw'

def convertSorted(token, line, t,v,i,understood, variables):
    type = getType(token, i+1, understood, variables)

    i+= 1
    t,v,_,_,_ = token[i]
    temp, i, understood, variables = convertGrouping(token,'',t,v,i,understood,variables)
    if type == 'LIST':
        line += 'sort ' + temp
    else:
        line += 'sort ' + temp
        understood = False
    return line, i, understood, variables
