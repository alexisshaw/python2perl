import keyword
import re
import tokenize
import convertToken

__author__ = 'Alexis Shaw'

def convertNot(token,line,t,v,i,understood,variables):
    """

    """
    line += '!('
    i += 1
    while len(token)-i > 0 :
        (t, v, _, _,_) = token[i]
        if t == tokenize.NAME and not keyword.iskeyword(v):
            line,i,understood,variables = convertToken.convertToken(token, line,t,v,i,understood,variables)
        elif t == tokenize.OP and re.match(r'^[<>&^|~=+*%,-]$|^\*\*$|<<|>>|>=|<=|!=|==',v):
            line,i,understood,variables = convertToken.convertToken(token, line,t,v,i,understood,variables)
        elif t == tokenize.NL or t == tokenize.NUMBER:
            line,i,understood,variables = convertToken.convertToken(token,line,t,v,i,understood,variables)
        elif t == tokenize.STRING:
            line,i,understood,variables = convertToken.convertToken(token,line,t,v,i,understood,variables)
        elif t == tokenize.COMMENT and token[i+1][0] == tokenize.NL:
            line,i,understood,variables = convertToken.convertToken(token,line,t,v,i,understood,variables)
        else:
            line += ') '
            return convertToken.convertToken(token,line,t,v,i,understood,variables)
        i += 1
