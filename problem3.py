
import math

def getLargestPrime(max):

	prime = 2
	x = 2
	while x <= max:
		if max % x == 0:
			prime = x
			max /= x
			x = x - 1
		else:
			x = x + 1

	return prime
			
print getLargestPrime(600851475143)



