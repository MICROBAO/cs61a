# Discussion 3: Recursion

# 1.1
def multiply(m, n):
	if m == 0 or n == 0:
		return 0
	return m + multiply(m, n - 1)

# 1.2
# Environment diagram; see handwritten page

# 1.3
def hailstone(n):
	print(n)
	if n == 1:
		return 1
	elif n % 2 == 0:
		return 1 + hailstone(n // 2)
	else:
		return 1 + hailstone(n * 3 + 1)

# 1.4
def is_prime(n):
	def prime_helper(k):
		if n == 1:
			return False
		elif k < n:
			if n % k == 0:
				return False
			return prime_helper(k + 1)
		else:
			return True
	return prime_helper(2)

# 1.5
def merge(n1, n2):
	if n1 == 0:
		return n2
	elif n2 == 0:
		return n1
	elif n1 % 10 < n2 % 10:
		return n1 % 10 + 10 * merge(n1 // 10, n2)
	else:
		return n2 % 10 + 10 * merge(n1, n2 // 10)

# 1.6
def make_func_repeater(f, x):
	def repeat(calls):
		if calls == 0:
			return x
		else:
			return f(repeat(calls - 1))
	return repeat












