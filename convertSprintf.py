from convertString import getString
import convertToken

__author__ = 'Alexis Shaw'

def convertSprintf(token,line,t,v,i,understood,variables):
    string,i,understood,variables = getString(token,line,t,v,i,understood,variables)
    i += 2
    t,v,_,_,_ = token[i]
    format,i,understood,variables = convertToken.convertToken(token,line,t,v,i, understood,variables,'')
    line += 'sprintf ('+string +', '+ format+' ) '

    return line, i, understood, variables

