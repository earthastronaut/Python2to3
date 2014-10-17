#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: This file was made to test the command line utility 2to3 which assists
in converting python 2 to python 3 code.
AUTHOR: Dylan Gregersen
DATE: Fri Oct 17 16:08:03 2014
"""
# `raw_input` is now use `input`
choose = raw_input("Please enter your name : ")
i = 2
o = input("input the letter i : ")

# % for formatting not supported
response = "Your name is %s" % choose

# print statement is not a function not a keyword
print response

# string formats
response = "variable {} equals {}".format(i,o)
print response 

# types
byte_form = 0222
print(type(10) is type(10L)) #  Python 2 has two different kinds of integer

# division not casts to a float by default
print 5/2
print 5//2

# some functions are now just generators
a = range(5)
print a
b = map(float,a)
print b
print zip(a,b)

mydict = {'pi':3.14159,'c':3e8,'e':2.7183}
mydict.iterkeys()
mydict.keys()

for i in range(5):
    print(i)

# changed this method
mydict.has_key('a')

# no more basestring
if isinstance("mystring",basestring):
    print("hello string")

# package renaming
# package support. pyport middy. 
# __init__

# callable 3.1
fxn = lambda x:2*x
if callable(fxn):
    print("lambda function is callable")

# converts syntax 
pi = 3.1415
pi <> 5

def fxn (a,b):
    return a+b

# enforce True and False as keywords
# True = 0
# False = 1
len = 3 # gotcha warning! 

# new style classes
class MyClass:
    pass

class MyType (object):
    pass

print type(MyClass)
print type(MyType)

# error handling
try:
    1/0
except ZeroDivisionError,e:
    print(e)

# END with other tips and tricks
# inpsect, dictionaries as matching?, *args**kwargs,








