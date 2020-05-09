# Discussion 9: Scheme

# 3.1
# scm> (define a (+ 1 2))
# a
# scm> a
# 3
# scm> (define b (+ (* 3 3) (* 4 4)))
# b
# scm> (+ a b)
# 28
# scm> (= (modulo 10 3) (quotient 5 3))
# #f
# scm> (even? (+ (- (* 5 4) 3) 2))
# #t

# 4.1
# scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
# 1
# scm> (if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2)))
# 10
# scm> ((if (< 4 3) + -) 4 100)
# -96
# scm> (if 0 1 2)
# 1

# 4.1
(define (factorial x) 
	(if (= x 1)
		(0)
		(* x (factorial (- x 1)))))

# 4.2
(define (fib n)
	(if (<= n 1)
		n
		(+ (fib (- n 1)) (fib (- n 2)))))

# 5.1
(define (my-append a b)
	(if (null? a)
		b
		(cons (car a) (my-append (cdr a) b))))

# Quarantine Dieting
# >>> a.k
# 2
# >>> b.k
# Error
# >>> VendingMachine.k
# 10
# >>> isinstance(b, VendingMachine)
# False
# >>> a is a.soda.machine
# True
# >>> VendingMachine is a.soda.machine
# False
# >>> c = VendingMachine
# >>> c.__init__(c, 11, True)
# False
# >>> c.soda.machine is VendingMachine
# True
# >>> a.k == c.k
# False
# >>> c.soda.machine.k
# 11



















