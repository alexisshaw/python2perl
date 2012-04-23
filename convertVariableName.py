import re
import tokenize
from convertGrouping import convertGrouping
from convertSprintf import convertSprintf
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
    if v in variables and variables[v] == 'STRING':
        if len(token) - i > 1 and token[i+1][0] == tokenize.OP and token[i+1][1] == '%':
            line, i, understood, variables = convertSprintf(token,line,t,v,i,understood,variables)
        else:
            line += '$' + v + ' '
    elif v in variables and variables[v] == 'NONSTRINGSCALAR':
        line += '$' + v + ' '
    elif v in variables and variables[v] == 'LIST':
        if token[i+1][0] == tokenize.OP and token[i+1][1] == '[':
            line += '@' + v
        elif token[i+1][0] == tokenize.OP and token[i+1][1]   == '.' and\
             token[i+2][0] == tokenize.NAME and token[i+2][1] == 'append'and\
             token[i+3][0] == tokenize.OP and token[i+3][1] == '(':
            toAppend, i, understood, variables = convertGrouping(token,line,t,v,i+3,understood,variables)
            line += 'push(@'+v+','+ toAppend + ') '
        elif token[i+1][0] == tokenize.OP and token[i+1][1]   == '.' and\
             token[i+2][0] == tokenize.NAME and token[i+2][1] == 'pop'and\
             token[i+3][0] == tokenize.OP and token[i+3][1] == '(' and\
             token[i+4][0] == tokenize.OP and token[i+4][1] == ')':
             line += 'pop(@' + v + ') '
             i += 4
        else:
            line += '@' + v + ' '
    elif v in variables and variables[v] == 'DICT':
        if token[i+1][0] == tokenize.OP and token[i+1][1] == '[':
            line += '%' + v
        elif token[i+1][0] == tokenize.OP and token[i+1][1]   == '.' and\
             token[i+2][0] == tokenize.NAME and token[i+2][1] == 'keys'and\
             token[i+3][0] == tokenize.OP and token[i+3][1] == '(' and\
             token[i+4][0] == tokenize.OP and token[i+4][1] == ')':
            line += 'keys(' + v + ') '
            i+= 4
        else:
            line += '%' + v + ' '
    else:
        line += '$' + v + ' '
    return line, i, understood, variables

def getType(token, i, understood, variables):
    if token[i][1] in variables:
        type = variables[token[i][1]]
        if type == 'LIST' and len(token)-i > 1 and token[i+1][1] =='[':
            if not re.match('\[[^\]:]*:[^\]]]',token[i][4]): #will incorrectly tag some situations
                type = 'NONSTRINGSCALAR'
        if type == 'DICT' and len(token)-i > 1 and token[i+1][1] =='[':
            type = 'NONSTRINGSCALAR'
        return type, understood
    elif token[i][0] == tokenize.OP and token[i][1] == '[':
        return 'LIST', understood
    elif token[i][0] == tokenize.OP and token[i][2] == '{':
        return 'DICT', understood
    elif token[i][0] == tokenize.OP and token[i][1] == '(' and len(token)-i > 1:
        return getType(token, i+1, understood,variables)
    elif token[i][0] == tokenize.NAME and token[i][1] == 'len':
        return 'NONSTRINGSCALAR', understood
    elif token[i][0] == tokenize.NAME and token[i][1] == 'sorted':
        return 'LIST', understood
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
        #print tokenize.tok_name[token[i][0]], token[i][1], understood, i
        return 'NOTKNOWN', False


