# -*- coding: utf-8 -*-
"""
This is basic math library
IVS Project 2
Author : Patrik Demský (xdemsk00)
Date : 9.4.2020
"""
#define + (add)
def add(x,y):
	return float(x + y)

#define - (subtract)
def sub(x,y):
	return float(x - y)

#define * (multiplication)
def mul(x,y):
	return float(x * y)

#define / (division)
def div(x,y):
	return float(x / float(y))

#define fact (factorial)
def fact(x):
	f=1
	if x == 0:
		f = 1
	else:
		for i in range(1,x+1):
			f=f*i
	return f

#define ** (exponentiation)
def exp(x,y):
	return float(x ** y)

#define // (extraction)
def ext(x,y):
	return float(x ** (1.0 / (y)))

#define abs (absolute value)
def abs(x):
	if x < 0:
		x = -x
	else:
		x = x
	return float(x)
