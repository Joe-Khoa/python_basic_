from math import *


angle =  float(input('enter angle : '))
sinx = sin(radians(angle))
cosx = cos(radians(angle))
tanx = tan(radians(angle))
cotanx = 1/tanx
print("sin({0}) = {1}".format(angle,sinx))
print("cos({0}) = {1}".format(angle,cosx))
print("tan({0}) = {1}".format(angle,tanx))
print("cotan({0}) = {1}".format(angle,cotanx))