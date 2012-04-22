import tokenize

__author__ = 'Alexis Shaw'

def convertLineEnd(token, line,t,v,i,understood,variables):
    """

    """
    if t == tokenize.NEWLINE and i >= 1 and token[i-1][0] != tokenize.COMMENT and token[i-1][1] != 'sys':
        line += ';'
    if not understood:
        line = '#'+line
    print line
    line = ''
    understood = True
    return line,i,understood,variables
