# Discussion 12

# 1.1
def paths(x, y):
	if x == y:
		return [[y]]
	elif x > y:
		return []
	else:
		a = paths(x + 1, y)
		b = paths(2 * x, y)
		return [[x] + subpath for subpath in a + b]

# 1.2
def mergesort(seq):
	if len(seq) <= 1:
		return seq
	else:
		mid = len(seq) // 2
		return merge(mergesort(seq[:mid]), mergesort(seq[mid:]))



# TREES






# 3.1
>>> cats = [1, 2]
>>> dogs = [cats, cats.append(23), list(cats)]
>>> cats
[1, 2, 23]

>>> dogs[1] = list(dogs)
>>> dogs[1]
[[1, 2, 23], None, [1, 2, 23]]

>>> dogs[0].append(2)
>>> cats
[1, 2, 23, 2]

>>> cats[1::2]
[2, 2]

>>> cats[:3]
[1, 2, 23]

>>> dogs[2].extend([list(cats).pop(0), 3])
>>> dogs[3]
Index Error

>>> dogs
[[1, 2, 23, 2], [[1, 2, 23, 2], None, [1, 2, 23, 1, 3]], [1, 2, 23, 1, 3]]






















