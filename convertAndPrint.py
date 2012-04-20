import re
from parseline import tabsToSpaces

__author__ = 'Alexis Shaw'

import array

def convertAndPrint(linesOfFile):
    lines = []
    for l in linesOfFile:
        lines.append(tabsToSpaces(l))

    if re.match("^#!", lines[0]):
        lines[0] = convertSheBang(lines[0])

    tokenList = getListOfTokens(lines);

