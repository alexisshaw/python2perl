import re
import tokenize
from convertSys import isReadlines, isReadline

__author__ = 'Alexis Shaw'

def convertVariableName(token,line,t,v,i,understood,variables):
    if token[i+1][0] == tokenize.OP and token[i+1][1] == '=':
        type,understood = getType(token , i+2, understood,variables)
        if not (v in variables) or type != variables[v]:
            variables[v] = type
            line += 'my '
    elif token[i-1][0] == tokenize.NAME and token[i-1][1] == 'for' and token[i+2][1] == 'range':
        if not (v in variables) or "NONSTRINGSCALAR" != variables[v]:
            variables[v] = "NONSTRINGSCALAR"
    if v in variables and re.match("^(STRING|NONSTRINGSCALAR)$",variables[v]):
        line += '$' + v + ' '
    elif v in variables and variables[v] == 'LIST':
        if token[i+1][0] == tokenize.OP and token[i+1][1] == '[':
            line += '$' + v
        else:
            line += '@' + v + ' '
    elif v in variables and variables[v] == 'DICT':
        if token[i+1][0] == tokenize.OP and token[i+1][1] == '[':
            line += '$' + v
        else:
            line += '%' + v + ' '
    else:
        line += '$' + v + ' '
    return line, i, understood, variables

def getType(token, i, understood, variables):
    if token[i][0] in variables:
        type = variables[token[i][0]]
        if type == 'LIST' and len(token)-i > 1 and token[i+1][1] =='[':
            type = 'NONSTRINGSCALAR'
        if type == 'HASH' and len(token)-i > 1 and token[i+1][1] =='[':
            type = 'NONSTRINGSCALAR'
        return type, understood
    elif token[i][0] == tokenize.OP and token[i][1] == '[':
        return 'LIST', understood
    elif token[i][0] == tokenize.OP and token[i][2] == '{':
        return 'DICT', understood
    elif token[i][0] == tokenize.OP and token[i][1] == '(' and len(token)-i > 1:
        return getType(token, i+1, understood,variables)
    elif isReadlines(token,i):
        return 'LIST', understood
    elif token [i][0] == tokenize.STRING:
        return 'STRING', understood
    elif isReadline(token,i):
        return 'STRING', understood
    elif token [i][0] == tokenize.NUMBER:
        return 'NONSTRINGSCALAR' , understood
    elif token [i][1] == 'int':
        return "NONSTRINGSCALAR", understood
    elif len(token)-i > 1 and \
         token[i][0]   == tokenize.NAME and token[i][1] in variables and \
         token[i+1][0] == tokenize.NEWLINE or token[i+1][0] == tokenize.COMMENT:
        return variables[token[i][1]], understood
    elif len(token)-i > 2 and\
         token[i][0]   == tokenize.NAME and token[i][1] in variables and\
         re.match("^(STRING|NONSTRINGSCALAR)$",variables[token[i][1]]):
        if variables[token[i][1]] == 'STRING' or getType(token, i+2, understood, variables)[0] == 'STRING':
            return 'STRING', understood
        else:
            return 'NONSTRINGSCALAR', understood
    else:
        print tokenize.tok_name[token[i][0]], token[i][1], understood, i
        return 'NOTKNOWN', False


