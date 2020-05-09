# Discussion 5: Data Abstraction, Trees, & Mutability

# 1.1
def height(t):
	if is_leaf(t):
		return 0
	return max([1 + height(b) for b in branches(t)])

# 1.2
def square_tree(t):
	square_br = [square_tree(b) for b in branches(t)]
	return tree(label(t) ** 2, branches=square_br)

# 1.3
def find_path(tree, x):
	if x == label(tree):
		return [x]
	for b in branches(tree):
		path = find_path(b, x)
		if path:
			return [label(tree)] + path

# 1.4
# t = tree(1, [tree(2), tree(3)])
# 1) label(t)
#    a) 1
#    b) Not an abstraction violation.
# 2) t[0]
#    a) 1
#    b) Yes, doesn't use the label abstraction.
# 3) label(branches(t)[0])
#    a) tree(2)
#    b) Not an abstraction violation.
# 4) label(branches(t))
#    a) tree(2)
#    b) Yes, it assumes that label gets the first element of a list.
# 5) is_leaf(t[1:][1])
#    a) True
#    b) Yes, it doesn't use the branches abstraction
# 6) [label(b) for b in branches(t)]
#    a) [2, 3]
#    b) Not an abstraction violation.
# 7) branches(tree(2, tree(t, [])))[0]
#    a) t
#    b) Yes, as a tree is passed as a list of branches.

# Section 2: Mutation
# Note that using the '+' operator on lists does not mutate the
# original list. However, using the '.append' method on a list
# will mutate it.
#
# List mutation methods:
# .append(el): Adds el to the end of the list, and returns None
# .extend(lst): Extends the list by concatenating it with lst, 
#              and returns None
# .insert(i, el): Insert el at index i (does not replace element 
#                but adds a new one), and returns None
# .remove(el): Removes the first occurrence of el in list, 
#              otherwise errors, and returns None
# .pop(i): Removes and returns the first occurence of el in list,
#          otherwise errors, and return None

# 2.1
# >>> lst1 = [1, 2, 3] 
# 
# >>> lst2 = lst1
# 
# >>> lst1 is lst2
# True
# >>> lst2.extend([5, 6])
#
# >>> lst1[4]
# 6
# >>> lst1.append([-1, 0, 1])
#
# >>> -1 in lst1
# False
# >>> lst2[5]
# [-1, 0, 1]
# >>> lst3 = lst2[:]
# 
# >>> lst3.insert(3, lst2.pop(3)) 
#
# >>> len(lst1)
# 5
# >>> lst1[4] is lst3[6]
# True
# >>> lst3[lst2[4][1]]
# 1
# >>> lst1[:3] is lst2[:3]
# False
# >>> lst1[:3] == lst2[:3]
# True
# >>> x = (1, 2, [4, 5, 6])
# 
# >>> x[2] = [3, 5, 6]
# Error: tuple not mutable
# >>> x
# (1, 2, [4, 5, 6])
# >>> x[2][0] = 3
# 
# >>> x
# (1, 2, [3, 5, 6])

# 2.2
def add_this_many(x, el, lst):
	for i in range(len(lst)):
		if lst[i] == x:
			lst.append(el)

# 2.3
def group_by(s, fn):
	d = {}
	for e in s:
		if fn(e) not in d:
			d[fn(e)] = [e]
		else:
			d[fn(e)].append(e)
	return d

# So Many Options...
# a)
def partition_options(total, biggest):
	if total == 0:
		return [[]]
	elif total < 0 or biggest == 0:
		return []
	else:
		with_biggest = partition_options(total - biggest, biggest)
		without_biggest = partition_options(total, biggest - 1)
		with_biggest = [[biggest] + elem for elem in with_biggest]
		return with_biggest + without_biggest
# b)
def min_elements(T, lst):
	if T == 0:
		return 0
	return min([1 + min_elements(T - el, lst) for el in lst if T - el >= 0])


## Tree Methods ##

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])