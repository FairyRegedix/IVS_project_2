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
	return float(x / y)

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
