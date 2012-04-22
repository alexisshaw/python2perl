#!/usr/bin/env python

#this is a comment it should be in the test file verbatim for "string" hello
import sys

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

print f , 'hello', 1 + (g + j) + k,

i = 0
if i == 0 : print i,
if i == 0 : i += 1; print i,
if i == 1:
    i += 2
    print i,
    print i+2

for i in range(1,5): print "hello"

sys.stdout.write('hello')
a = sys.stdin.readline()

print int(5.43) + 4

print a


