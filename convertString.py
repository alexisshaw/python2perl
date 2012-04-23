import re
import tokenize
import convertSprintf

__author__ = 'Alexis Shaw'

def convertString(token,line, t, v, i, understood, variables):
    if len(token) - i > 1 and token[i+1][0] == tokenize.OP and token[i+1][1] == '%':
        return convertSprintf.convertSprintf(token,line,t,v,i,understood,variables)
    else:
        return getString(token,line,t,v,i,understood,variables)


def getString(token,line,t,v,i,understood,variables):
    if re.match('^(["|\'])(.*)\\1$', v):
        if re.match("^'.*'$",v): v = re.sub('"',r'\"',v)
        string = re.sub('^(["|\'])(.*)\\1$',r'"\2"',v)
        string = re.sub('(\$|@|%)',r'\\\1',string)
    elif re.match("^[rR](['|\"])(.*)\\1$", v):
        if re.match(r'^[rR]".*"$', v):
            v = re.sub("'",r"\'",v)
            v = re.sub(r"\"", r'"',v)
        string = re.sub("^[rR](['|\"])(.*)\\1$", r"'\2'",v)
    else:
        string = v


    line += string + ' '
    if token[i+1][0] == tokenize.COMMENT and\
       token[i+2][0] == tokenize.NL and\
       token[i+3][0] == tokenize.STRING:
        line += '. '
    elif token[i+1][0] == tokenize.NL and\
         token[i+2][0]  == tokenize.STRING:
        line += '. '
    elif token[i+1][0] == tokenize.STRING:
        line += '. '
    return line, i, understood, variables
