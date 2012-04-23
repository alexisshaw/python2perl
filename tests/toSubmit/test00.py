#!/usr/bin/env python

#this is a comment it should be in the test file verbatim for "string" hello

a = "He$a\tllo"
b = 'He$a\tllo'
c = r'He$a\tllo'
d = R'He$a\tllo'
e = r"He$a\tllo"
f = R"He$a\tllo"
print a, b, c, d, e, f,

print a + b + (c + d) + (e + f)

g = 0.1
h = 1
j = 0.2
k = 4.5

print g, "hello", g, j, k

print a + 'hello', 1 + (g + j) + k,


