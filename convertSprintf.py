import re
import convertString
import convertToken

__author__ = 'Alexis Shaw'

def convertSprintf(token,line,t,v,i,understood,variables):
    string,i,understood,variables = convertString.getString(token,'',t,v,i,understood,variables)
    i += 2
    t,v,_,_,_ = token[i]
    format,i,understood,variables = convertToken.convertToken(token,'',t,v,i, understood,variables,'')
    i +=1
    t,v,_,_,_ = token[i]
    string = re.sub(r'\\(%|$|@)', r'\1', string)
    line += 'sprintf ('+string +', '+ format+' ) '

 #   print tokenize.tok_name[t], i

    return line, i, understood, variables

