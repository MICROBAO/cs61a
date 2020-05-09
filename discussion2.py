# Discussion 2: HOF, Self Reference

# 1.1
# Environment diagram; see handwritten page

# 1.2
curry2 = lambda h: lambda x: lambda y: h(x, y)

# 1.3
# Environment diagram; see handwritten page

# 1.4
# Environment diagram; see handwritten page

# 1.5
def keep_ints(cond, n):
	k = 1
	while k <= n:
		if cond(k) == True:
			print(k)
		k += 1

# 1.6
def make_keeper(n):
	def do_keep(cond):
		k = 1
		while k <= n:
			if cond(k) == True:
				print(k)
			k += 1
	return do_keep

# 2.1
def print_delayed(x):
	def delay_print(y):
		print(x)
		return print_delayed(y)
	return delay_print

# 2.2
def print_n(n):
	def inner_print(x):
		if n <= 0:
			print("done")
		else:
			print(x)
		return print_n(n - 1)
	return inner_print

# Quiz: environment diagram
# See handwritten page
















