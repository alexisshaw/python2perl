import re
import tokenize
import convertToken

__author__ = 'Alexis Shaw'

def convertSliceOperator(token,line,t,v,i,understood,variables):
    sliceOperators = []
    count = 0

    i+=1
    sliceOperators.append('')
    while len(token)-i > 0 :
        (t, v, _, _,_) = token[i]
        if t == tokenize.NAME:
            sliceOperators[count],i,understood,variables = convertToken.convertToken(token, sliceOperators[count],t,v,i,understood,variables,'')
        elif t == tokenize.OP and re.match(r'^[([<>&^|~=+,*%-]$|^\*\*$|<<|>>|>=|<=|!=|==',v):
            sliceOperators[count],i,understood,variables = convertToken.convertToken(token, sliceOperators[count],t,v,i,understood,variables,'')
        elif t == tokenize.NL or t == tokenize.NUMBER:
            sliceOperators[count],i,understood,variables = convertToken.convertToken(token,sliceOperators[count],t,v,i,understood,variables,'')
        elif t == tokenize.STRING:
            sliceOperators[count],i,understood,variables = convertToken.convertToken(token,sliceOperators[count],t,v,i,understood,variables,'')
        elif t == tokenize.COMMENT and token[i+1][0] == tokenize.NL:
            sliceOperators[count],i,understood,variables = convertToken.convertToken(token,sliceOperators[count],t,v,i,understood,variables,'')
        elif t == tokenize.OP and v == ']':
            break
        elif t == tokenize.OP and v == ':':
            sliceOperators.append('')
            count+= 1
        else: understood = False
        i += 1
    if len(sliceOperators) == 1:
        line += '['+sliceOperators[0]+'] '
    elif len(sliceOperators) == 2:
        if sliceOperators[0] == '':
            sliceOperators[0] = '0'
        if sliceOperators[1] == '':
            sliceOperators[1] = '-1'
        line += '['+sliceOperators[0]+'..'+sliceOperators[1]+']'
    elif len(sliceOperators) == 3:
        line += '['+sliceOperators[0]+'..'+sliceOperators[1]+'..'+sliceOperators[2]+']'
        understood == False
    return line, i, understood, variables,count



