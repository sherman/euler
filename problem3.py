
def xlongrange(start, limit, step):
	n = start

	if n < limit:
		while n < limit:
			yield n
			n += step
	else:
		while n > limit:
			yield n
			n += step

def isPrimeNumber(number):
	if number % 2 == 0 or number % 3 == 0:
		return False

	k = 6
	while ((k - 1) * (k - 1)) <= number:
		if number % (k - 1) == 0 or number % (k + 1) == 0:
			return False;

		k += 6
	
	return True

def findMaxFactor(number):
	maxFactor = None
	for elt in xlongrange(number, 2, -1):
		if elt % 2 == 0 or elt % 3 == 0:
			continue

		if number % elt == 0:
			if isPrimeNumber(elt):
				return elt
	
		#print elt
	return None
				
 
#print findMaxFactor(13195)
#print findMaxFactor(600851475143)
original = 600851475143
limit = 600851475143 / 2

curr = limit
while curr > 0:
	if original % curr == 0:
		print curr
		if isPrimeNumber(curr):
			print curr
			break

	curr = curr - 1

#for elt in xlongrange(limit, 2, -1):
#	print elt
#	if original % elt == 0:
#		print elt
		#if isPrimeNumber(elt):
		#	print elt
#	else:
#		limit = elt / 2


