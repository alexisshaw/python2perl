import re

def tabsToSpaces(line):
    noSpacesSoFar = 0
    noSpacesToAdd = 0
    for c in line:
        if c == ' ':
            noSpacesSoFar += 1
        elif c == '\t':
            noSpacesToAdd += 8 - noSpacesSoFar%8
            noSpacesSoFar += 8 - noSpacesSoFar%8
        else:
            break
    spaces = ''.join(['' for i in xrange(noSpacesToAdd)])
    re.sub("\t","")
    return spaces + line



