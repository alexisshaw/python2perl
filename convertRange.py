import tokenize
from getFunctionExpression import getFunctionExpression

__author__ = 'Alexis Shaw'

def convertRange(token, line, t,v,i,understood, variables):
    iOrig = i
    i += 1
    if v!= 'range':
        print 'error'
        return
    t,v,_,_,_ = token[i]
    number1 = ''
    number2 = ''
    number3 = ''
    maxCount = 0
    if t == tokenize.OP and v == '(':
        maxCount = 1
        i += 1
        number1, i, understood,variables =  getFunctionExpression(token, number1,t,v,i,understood,variables, '')
        if token[i-1][1] == ',':
            maxCount = 2
            number2, i, understood,variables =  getFunctionExpression(token, number2,t,v,i,understood,variables, '')
        if token[i-1][1] == ',':
            maxCount = 3
            number3, i, understood,variables =  getFunctionExpression(token, number3,t,v,i,understood,variables, '')
    if maxCount == 1:
        line += '(0 .. '+ number1 + '+ 1 ) '
        i -= 1
    elif maxCount == 2:
        line += '(' + number1 + '.. ' + number2 + '- 1 )'
        i -= 1
    else:
        understood = False
        i = iOrig
    return line,i,understood,variables






