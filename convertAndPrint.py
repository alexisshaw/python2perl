import tokenize
from convertToken import convertToken

def convertAndPrint(f):
    """
    Converts a python program file into perl program file
    """
    g = tokenize.generate_tokens(f.readline)
    token = []
    for l in g:
        token.append(l)
    line = ""
    understood = True
    variables = {}
    i=0
    (t, v, _, _,_) = token[i]
    while len(token)-i > 0:
        (t, v, _, _,_) = token[i]
        line,i,understood,variables = convertToken(token,line,t,v,i,understood,variables)
        i += 1



