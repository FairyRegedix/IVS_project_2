# -*- coding: utf-8 -*-
"""Math library for ivs project 2

Todo:
	-propperly handle root extraction in math_lib.exp()	

Author:
	Patrik Demský xdemsk00
	Denis Dzíbela xdzibe00

Date:
	9.4.2020
"""

import cmath

#define + (add)
def add(x, y):
	"""Simple addition function.

	x (float): first operand
	y (float): second operand

	Returns:
		float: sum of operands

	"""
	return float(x + y)

#define - (subtract)
def sub(x, y):
	"""Simple subtraction function.

	x (float): minuend (the number subtracted from)
	y (float): subtrahend (the number being subtracted)

	Returns:
		float: difference of operands

	"""
	return float(x - y)

#define * (multiplication)
def mul(x, y):
	"""Simple multiplication function.

	x (float): first operand
	y (float): second operand

	Returns:
		float: multiplication product of operands

	"""
	return float(x * y)

#define / (division)
def div(x, y):
	"""Simple division function.

	x (float): divident
	y (float): divisor

	Raises:
		ZeroDivisionError: if `y` is equal to 0

	Returns:
		float: division product of operands

	"""
	return float(x / float(y))

#define fact (factorial)
def fact(x):
	"""Simple factorial function.

	x (int): first operand

	Raises:
		ValueError: if `x` is not a positive integer

	Returns:
		int: `x` factorial (x!)
	"""
	#only defined for positive integers
	if x < 0 or isinstance(x, int) == False:
		raise ValueError

	f = 1
	#0! == 1
	if x == 0:
		return f
	else:
		for i in range(1,x+1):
			f=f*i
	return f

#define ** (exponentiation)
def exp(x, y):
	#TODO propperly handle root extraction
	"""Simple division function.

	x (float): base
	y (float): exponent

	Returns:
		float: `x` raised to the power of `y`

	"""

	return x ** y

#define // (extraction)
def ext(x, y):
	"""Simple root extraction function.

	x (float): radicand
	y (float): degree

	Raises:
		ValueError: if `x` < 0 and y is an even number
		ZeroDivisionError: if `y` is equal to 0 

	Returns:
		float: `y`-th root of `x`

	"""
	if x < 0 and y % 2 == 0:
		raise ValueError
	elif x < 0 and y % 2 != 0:
		z = ((x) ** (y ** -1))
		z = ((z.real ** 2) + (z.imag ** 2))** 0.5
		return -z #<- HACK, wtf

	return (x ** (1.0 / (y)))

#define abs (absolute value)
def abs(x):
	"""Simple absolute value function.

	x (float): first operand

	Returns:
		float: absolute value of `x`

	"""
	if x < 0:
		x = -x

	return float(x)
