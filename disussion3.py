# # Discussion 2

# 1.1
def multiply(m, n):
	if m == 0 or n == 0:
		return 0
	return m + multiply(m, n - 1)