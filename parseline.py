import re

def tabsToSpaces(line):
    """
    Converts tabs at the beginning of a line into spaces according to python specs
    """
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
    spaces = ''.join(['' for _ in xrange(noSpacesToAdd)])
    line = re.sub("\t","", line)
    return spaces + line



