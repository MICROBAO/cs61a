# OOP, Linked Lists, Efficiency

# 1.1
# >>> snape = Professor("Snape")
#
# >>> harry = Student("Harry", snape)
# There are now 1 students
# >>> harry.visit_office_hours(snape)
# Thanks, Snape
# >>> harry.visit_office_hours(Professor("Hagrid"))
# Thanks, Hagrid
# >>> harry.understanding
# 2
# >>> [name for name in snape.students]
# ['Harry']
# >>> x = Student("Hermione", Professor("McGonagall")).name
# There are now 2 students
# >>> x
# 'Hermione'
# >>> [name for name in snape.students]
# ['Harry']

# 1.2
class Email:
	def __init__(self, msg, sender_name, recipient_name):
		self.msg = msg
		self.sender_name = sender_name
		self.recipient_name = recipient_name

class Server:
	def __init__(self):
		self.clients = {}

	def send(self, email):
		self.clients[email.recipient_name].receive(email)

	def register_client(self, client, client_name):
		self.clients[client_name] = client

class Client:
	def __init__(self, server, name):
		self.inbox = []
		self.server = server
		self.name = name
		self.server.register_client(self, self.name)

	def compose(self, msg, recipient_name):
		self.server.send(Email(msg, self.name, recipient_name))

	def receive(self, email):
		self.inbox.append(email)

# 2.1
class Cat(Pet):
	def __init__(self, name, owner, lives=9):
		Pet.__init__(self, name, owner)
		self.lives = lives
	
	def talk(self):
		print(self.name + ' says meow!')

	def lose_life(self):
		if self.lives > 0:
			self.lives -= 1
			if self.lives == 0:
				self.is_alive = False
		else:
			print('This cat has no more lives to lose :(')

# 2.2
class NoisyCat(Cat):
	# __init__ method not necessary b/c NoisyCat already
	# inherits Cat's __init__ method.
	def talk(self):
		Cat.talk(self)
		Cat.talk(self)

# 2.3
# >>> x, y = A(), B() 
# >>> x.f()
# 2
# >>> B.f()
# Error: no self argument
# >>> x.g(x, 1)
# 4
# >>> y.g(x, 2)
# 8

# 3.1
def sum_nums(lnk):
	if lnk == Link.empty:
		return 0
	return lnk.first + sum_nums(lnk.rest)

# 3.2
def multiply_lnks(lst_of_lnks):
	product = 1
	for lnk in lst_of_lnks:
		if lnk is Link.empty:
			return Link.empty
		product *= lnk.first
	rests = [lnk.rest for lnk in lst_of_lnks]
	return Link(product, multiply_lnks(rests))

# 3.3
def filter_link(link, f):
	while link is not Link.empty:
		if f(link.first):
			yield link.first
		link = link.rest

def filter_no_iter(link, f):
	if link is Link.empty:
		return None
	elif f(link.first):
		yield link.first
	return filter_no_iter(link.rest, f)

# Midterm Review Snax
def feed(snax, x, y):
	def helper(lst, p, q):
		if not lst:
			return 0
		elif p < 0 or q < 0:
			return float('inf')
		elif len(lst) == 1:
			return not (p >= lst[0] or q >= lst[0])
		else:
			a = helper(lst[1:-1], p - lst[0], q - lst[-1]) 
			b = 2 + helper(lst[1:-1, x - lst[0], y - lst[-1]])
			c = 1 + helper(lst[1:-1, x - lst[0], q - lst[-1]])
			d = 1 + helper(lst[1:-1, p - lst[0], y - lst[-1]])
			return min(a, b, c, d)
		return helper(snax, 0, 0)

# Linked List Implementation
class Link:
	empty = ()
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

	def __repr__(self):
		if self.rest:
			rest_str = ', ' + repr(self.rest)
		else:
			rest_str = ''
		return 'Link({0}{1})'.format(repr(self.first), rest_str)


	def __str__(self): 
		string = '<'
		while self.rest is not Link.empty: 
			string += str(self.first) + ' '
			self = self.rest
		return string + str(self.first) + '>'








		