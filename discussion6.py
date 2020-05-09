# Discussion 6: Nonlocal, Iterators, & Generators

# Section 1: Nonlocal
# The nonlocal keyword is used to modify a binding in a parent
# frame. However there are two important caveats:
#       1) Global names cannot be modified using nonlocal.
#       2) Names in the current frame cannot be overriden
#          using the nonlocal keyword. This means we cannot
#          have both a local and nonlocal binding for the same
#          name in a single frame.
# Functions using nonlocal are called mutable functions.

# 1.1
# Environment diagram; see handwritten notes.

# 1.2
def memory(n):
	def updater(fn):
		nonlocal n
		n = fn(n)
		return n
	return updater

# 1.3
def nonlocalist():
	get = lambda x: 'Index out of range!'
	def prepend(value):
		nonlocal get 
		f = get
		def get(i):
			if i == 0:
				return value
			return f(i - 1)
	return prepend, lambda x: get(x)

# Section 2: Iterators
# Calling the 'iter' function on an iterable will create an
# iterator over that iterable. Calling the 'next' function on an
# iterator will give the current value in the iterable and
# move the iterator's position to the next value.

# 2.1
# >>> lst = [6, 1, "a"] 
# 
# >>> next(lst)
# Error: a list is not an iterator, it is an iterable.
# >>> lst_iter = iter(lst)
#
# >>> next(lst_iter)
# 6
# >>> next(lst_iter)
# 1
# >>> next(iter(lst))
# 6
# >>> [x for x in lst_iter]
# ["a"]

# Section 3: Generators
# A generator function uses a 'yield' statement instead of a
# return statement. When a generator function is called, it
# returns a generator object, which is a type of iterator.
#
# A generator function can have multiple yield statements.
# When 'next' is called again, execution resumes where it
# stopped last and continues until the next 'yield' or the
# end of the function.
# 
# When 'yield from' is called on an iterator, it will yield
# every value from that iterator.
# i.e. it is the same as:
#             for x in an_iterator:
#                 yield x

# 2.1
def merge(a, b):
	first_a, first_b = next(a), next(b)
	while True:
		if first_a < first_b:
			yield first_a
			first_a = next(a)
		elif first_b < first_a:
			yield first_b
			first_b = next(b)
		else:
			yield first_a
			first_a, first_b = next(a), next(b)

# 2.2
def generate_subsets():
	subsets = [[]]
	n = 1
	while True:
		yield subsets 
		subsets = subsets + [s + [n] for s in subsets]
		n += 1

# 2.3
def sum_paths_gen(t):
	if is_leaf(t):
		yield label(t) 
	for br in branches(t):
		for s in sum_paths_gen(br):
			yield s + label(t)

# Trie Recursion
def collect_words(t):
	if is_leaf(t):
		return [label(t)]
	words = []
	for br in branches(t):
		words += [label(t) + word for word in collect_words(br)]
	return words























