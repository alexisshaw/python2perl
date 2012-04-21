import tokenize
from tokenize import generate_tokens

from convertToken import convertToken

def convertAndPrint(f):
    """
    Converts a python program file into perl program file
    """
    g = generate_tokens(f.readline)
    token = []
    for l in g:
        token.append(l)
    line = ""
    understood = True
    variables = {}
    i=0
    (t, v, _, _,_) = token[i]
    while t != tokenize.ENDMARKER:
        line,i,understood,variables = convertToken(token,line,t,v,i,understood,variables)
        i += 1
        (t, v, _, _,_) = token[i]



