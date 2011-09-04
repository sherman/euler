
def xlongrange(start, limit, step):
	n = start
	while n < limit:
		yield n
		n += step

def isPrimeNumber(number):
	for elt in xlongrange(2, number, 1):
		if number % elt == 0:
			return False
		
	return True

def findMaxFactor(number):
	maxFactor = None
	for elt in xlongrange(2, number, 1):
		if number % elt == 0:
			if isPrimeNumber(elt):
				maxFactor = elt
	
	return maxFactor
				
 
print findMaxFactor(600851475143)

