import re
import tokenize
import convertToken

__author__ = 'Alexis Shaw'

def getFunctionExpression(token, line,t,v,i,understood,variables, oldIdent):
    while len(token)-i > 0 :
        (t, v, _, _,_) = token[i]
        if t == tokenize.NAME:
            line,i,understood,variables = convertToken.convertToken(token, line,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.OP and re.match(r'^[([\]<>&^|~=+*%[-]$|^\*\*$|<<|>>|>=|<=|!=|==',v):
            line,i,understood,variables = convertToken.convertToken(token, line,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.NL or t == tokenize.NUMBER:
            line,i,understood,variables = convertToken.convertToken(token,line,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.STRING:
            line,i,understood,variables = convertToken.convertToken(token,line,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.COMMENT and token[i+1][0] == tokenize.NL:
            line,i,understood,variables = convertToken.convertToken(token,line,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.OP and re.match('[,)]', v):
            break
        else: understood = False
        i += 1
    i += 1
    return line,i,understood,variables

