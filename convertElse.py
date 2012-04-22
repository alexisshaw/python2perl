import tokenize
from convertSuite import convertSuite

__author__ = 'Alexis Shaw'

def convertElse(token,line,t,v,i,understood,variables, oldIdent):
    """

    """
    condition = ''
    i += 1
    while len(token)-i > 0 :
        (t, v, _, _,_) = token[i]
        if t == tokenize.OP and v == ":":
            break
        i += 1
    i += 1
    (t, v, _, _,_) = token[i]
    body, i,understood,variables, singleLine, noSimpleStatements, comment = convertSuite(token,t,v,i,understood,variables, oldIdent)
    if singleLine:
        line += 'else {' + body + '}' + comment + '\n'
    else:
        line += 'else {\n' + body + '\n'+ oldIdent+'}\n'+ oldIdent

    return line, i, understood, variables
