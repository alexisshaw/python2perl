__author__ = 'Alexis Shaw'

from abc import ABCMeta, abstractproperty

class token:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._tokenType = ""
        self._tokenString = ""

    def getTokenType(self):
        return self._tokenType;
    def getTokenString(self):
        return self._tokenString
    def setTokenString(self, value):
        self._tokenString = value
    def delTokenString(self):
        del self._tokenString

    tokenType = abstractproperty(getTokenType)
    tokenString = abstractproperty(getTokenString, setTokenString, delTokenString, "The contents of the token")

class StringToken(token):

    def __init__(self):
        self._tokenType = "STRING"
        self._tokenString = ""

    def getTokenType(self):
        return self._tokenType;
    def getTokenString(self):
        return self._tokenString
    def setTokenString(self, value):
        self._tokenString = value
    def delTokenString(self):
        del self._tokenString

class printToken(token):
    def __init__(self):
        self._tokenType = "PRINT"
        self._tokenString = "print"

    def getTokenType(self):
        return self._tokenType;
    def getTokenString(self):
        return self._tokenString
    def setTokenString(self, value):
        self._tokenString = value
    def delTokenString(self):
        del self._tokenString

class newlineToken(token):
    def __init__(self):
        self._tokenType = "NEWLINE"
        self._tokenString = "\n"

    def getTokenType(self):
        return self._tokenType;
    def getTokenString(self):
        return self._tokenString
    def setTokenString(self, value):
        self._tokenString = value
    def delTokenString(self):
        del self._tokenString

class whiteSpaceToken(token):
    def __init__(self):
        self._tokenType = "WHITESPACE"
        self._tokenString = ""

    def getTokenType(self):
        return self._tokenType;
    def getTokenString(self):
        return self._tokenString
    def setTokenString(self, value):
        self._tokenString = value
    def delTokenString(self):
        del self._tokenString

class commentToken(token):
    def __init__(self):
        self._tokenType = "COMMENT"
        self._tokenString = ""

    def getTokenType(self):
        return self._tokenType;
    def getTokenString(self):
        return self._tokenString
    def setTokenString(self, value):
        self._tokenString = value
    def delTokenString(self):
        del self._tokenString
