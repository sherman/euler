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

print getNumber()
