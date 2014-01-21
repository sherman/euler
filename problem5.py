import math

def getNumber():
	x = 20
	while True:
		next = False
		for d in [20, 19, 18, 17, 16, 15, 14, 13, 11]:
			if x % d != 0:
				next = True
				break;

		if next == False:
			break;

		x = x + 20

	return x

def gcd(a, b):
	if a == b:
		return a

	while b > 0:
		a, b = b, a % b
	
	return a

def lcm(a, b):
	return abs(a * b) /	gcd(a, b);

def getNumberLcm(a, b):
	return reduce(lcm, range(a, b + 1))

print getNumberLcm(1, 20)
