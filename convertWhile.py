import re
import tokenize
from convertSuite import convertSuite
import convertToken

__author__ = 'Alexis Shaw'

def convertWhile(token,line,t,v,i,understood,variables, oldIdent):
    """

    """
    condition = ''
    i += 1
    while len(token)-i > 0 :
        (t, v, _, _,_) = token[i]
        if t == tokenize.NAME:
            condition,i,understood,variables = convertToken.convertToken(token, condition,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.OP and re.match(r'^[()[\]<>&^|~=+*%,/-]$|^\*\*$|<<|>>|>=|<=|!=|==',v):
            condition,i,understood,variables = convertToken.convertToken(token, condition,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.NL or t == tokenize.NUMBER:
            condition,i,understood,variables = convertToken.convertToken(token,condition,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.STRING:
            condition,i,understood,variables = convertToken.convertToken(token,condition,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.COMMENT and token[i+1][0] == tokenize.NL:
            condition,i,understood,variables = convertToken.convertToken(token,condition,t,v,i,understood,variables, oldIdent)
        elif t == tokenize.OP and v == ":":
            break
        i += 1
    i += 1
    (t, v, _, _,_) = token[i]
    body, i,understood,variables, singleLine, noSimpleStatements, comment = convertSuite(token,t,v,i,understood,variables, oldIdent)

    if singleLine and noSimpleStatements <= 1:
        line += body + ' ' + 'while ' + condition + ';' + comment + '\n'
    elif singleLine:
        line += 'while (' + condition + ') {' + body + '}' + comment + '\n'
    else:
        line += 'while (' + condition + ') {\n' + body + '\n'+ oldIdent+ '}\n' + oldIdent

    return line, i, understood, variables



