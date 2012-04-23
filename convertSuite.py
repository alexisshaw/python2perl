import re
import tokenize
import convertToken

__author__ = 'Alexis Shaw'

def convertSuite(token,t,v,i,understood,variables, oldIdent):
    endOfLine = ""
    singleLine = True
    if t == tokenize.COMMENT:
        endOfLine += v
        i += 1
        (t, v, _, _,_) = token[i]
    if t == tokenize.NEWLINE or t == tokenize.NL:
        singleLine = False
        i += 1
    body = ''
    indentValue = oldIdent
    noSimpleStatements = 1
    while len(token)-i > 0 :
        (t, v, _, _,_) = token[i]
        if t == tokenize.NAME:
            body,i,understood,variables = convertToken.convertToken(token, body,t,v,i,understood,variables, indentValue)
        elif t == tokenize.OP and re.match(r'^[()<>&^|~=+*[\]%,/-]$|^\*\*$|<<|>>|>=|<=|!=|==|\+=|-=|\*=|%=|&=',v):
            body,i,understood,variables = convertToken.convertToken(token, body,t,v,i,understood,variables, indentValue)
        elif t == tokenize.NUMBER:
            body,i,understood,variables = convertToken.convertToken(token, body,t,v,i,understood,variables, indentValue)
        elif t == tokenize.STRING:
            body,i,understood,variables = convertToken.convertToken(token, body,t,v,i,understood,variables, indentValue)
        elif t == tokenize.COMMENT and token[i+1][0] == tokenize.NL:
            temp,i,understood,variables = convertToken.convertToken(token, "",t,v,i,understood,variables, indentValue)
            if singleLine:
                endOfLine += temp
            else:
                body += temp
        elif t == tokenize.NEWLINE or t == tokenize.ENDMARKER or t == tokenize.NL:
            if singleLine:
                break
            else:
                if t == tokenize.NEWLINE and i >= 1 and token[i-1][0] != tokenize.COMMENT:
                    body += ';'
                if not understood:
                    body = '#'+body
                if t == tokenize.NEWLINE and i >= 1 and token[i+1][0] != tokenize.DEDENT:
                    body += '\n'
                    body += indentValue
        elif t == tokenize.INDENT:
            indentValue = v
            body += indentValue
        elif t == tokenize.DEDENT:
            if not singleLine:
                body += v
                break
        elif t == tokenize.OP and v == ';':
            body += v + ' '
            if singleLine:
                noSimpleStatements += 1

        i += 1
    return body, i,understood,variables, singleLine, noSimpleStatements, endOfLine
