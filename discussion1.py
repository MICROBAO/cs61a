# Discussion 1: Control, Environment Diagrams

# 1.1
def wears_jacket_with_if(temp, raining):
	if temp < 60 or raining:
		return True
	else:
		return False

def wears_jacket(temp, raining):
	return temp < 60 or raining

# 1.2
# >>> square(so_slow(5))
# Error: infinite loop. x will always be greater
# than zero so we never exit the loop and never
# execute x / 0.

# 1.3
def is_prime(n):
	if n == 1:
		return False
	i = 2
	while i < n:
		if n % i == 0:
			return False
		else:
			i += 1
	return True

# 2.1
# Environment diagram; see handwritten page

# 2.2
# Environment diagram; see handwritten page

# 2.3
# Environment diagram; see handwritten page

# 2.4
# Environment diagram; see handwritten page

# Quiz: WWPD
# See handwritten page





