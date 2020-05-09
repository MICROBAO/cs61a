# Discussion 4: Python Lists, Tree Recursion

# 1.1
def count_stair_ways(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	return count_stair_ways(n - 1) + count_stair_ways(n - 2)

# 1.2
def count_k(n, k):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		total = 0
		i = 1
		while i <= k:
			total += count_k(n-i, k)
			i += 1
		return total

# 2.1
# >>> a = [1, 5, 4, [2, 3], 3]
# >>> print(a[0], a[-1])
# 1 3 

# >>> len(a)
# 5

# >>> 2 in a
# False

# >>> 4 in a
# True

# >>> a[3][0]
# 2

# 2.2
def even_weighted(s):
	return [i * s[i] for i in range(len(s)) if i % 2 == 0]

# 2.3
def max_products(s):
	if not s:
		return 1
	elif len(s) == 1:
		return s[0]
	return max(max_products(s[1:]), s[0] * max_products(s[2:]))

# Whole Numbers
# a)
def check_hole_number(n):
	if n // 10 == 0:
		return True
	return (n % 10) > ((n // 10) % 10) \
		and (n // 100) > ((n // 10) % 10) \
		and check_hole_number(n // 100)

# b)
def check_mountain_number(n):
	def helper(x, increasing):
		if x // 10 == 0:
			return True
		if increasing and (x % 10) < ((x // 10) % 10):
			return helper(x // 10, increasing)
		return (x % 10) > ((x // 10) % 10) and helper(x // 10, False) 
	return helper(n, True)










