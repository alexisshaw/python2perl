import re
import tokenize
from convertSuite import convertSuite
import convertToken

__author__ = 'Alexis Shaw'

def convertFor(token,line,t,v,i,understood,variables):
    """

    """
    target = ''
    i += 1
    while len(token)-i > 0 :
        (t, v, _, _,_) = token[i]
        if t == tokenize.NAME:
            if v == 'in':
                break
            target,i,understood,variables = convertToken.convertToken(token, target,t,v,i,understood,variables)
        elif t == tokenize.OP and re.match(r'^[<>&^|~=+*%,/-]$|^\*\*$|<<|>>|>=|<=|!=|==',v):
            target,i,understood,variables = convertToken.convertToken(token, target,t,v,i,understood,variables)
        elif t == tokenize.NL or t == tokenize.NUMBER:
            target,i,understood,variables = convertToken.convertToken(token,target,t,v,i,understood,variables)
        elif t == tokenize.STRING:
            target,i,understood,variables = convertToken.convertToken(token,target,t,v,i,understood,variables)
        elif t == tokenize.COMMENT and token[i+1][0] == tokenize.NL:
            target,i,understood,variables = convertToken.convertToken(token,target,t,v,i,understood,variables)
        else:
            understood = False
        i += 1
    source = ''
    i += 1
    while len(token)-i > 0 :
        (t, v, _, _,_) = token[i]
        if t == tokenize.NAME:
            source,i,understood,variables = convertToken.convertToken(token, source,t,v,i,understood,variables)
        elif t == tokenize.OP and re.match(r'^[()<>&^|~=+*%,/-]$|^\*\*$|<<|>>|>=|<=|!=|==',v):
            source,i,understood,variables = convertToken.convertToken(token, source,t,v,i,understood,variables)
        elif t == tokenize.NL or t == tokenize.NUMBER:
            source,i,understood,variables = convertToken.convertToken(token,source,t,v,i,understood,variables)
        elif t == tokenize.STRING:
            source,i,understood,variables = convertToken.convertToken(token,source,t,v,i,understood,variables)
        elif t == tokenize.COMMENT and token[i+1][0] == tokenize.NL:
            source,i,understood,variables = convertToken.convertToken(token,source,t,v,i,understood,variables)
        elif t == tokenize.OP and v == ":":
            break
        else: understood = False
        i += 1
    i += 1
    (t, v, _, _,_) = token[i]
    body, i,understood,variables, singleLine, noSimpleStatements, comment = convertSuite(token,t,v,i,understood,variables)

    if singleLine:
        line += 'foreach ' + target + ' (' + source +'){' + body + '}' + comment + '\n'
    else:
        line += 'foreach ' + target + ' (' + source +'){\n' + body + '\n}\n'

    return line, i, understood, variables



