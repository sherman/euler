
def fib(max):
	a = 0
	b = 1
	x = 0

	for elt in range(max):
		if x >= max:
			break

		if a % 2 == 0:
			x += a

		a = a + b
		b = a - b
		
	return x

print fib(4000000)
