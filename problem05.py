"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that
pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    return lambda f : f(a, b)
Implement car and cdr.

"""

def cons(a, b):
	return lambda f: f(a, b)

def car(f):
	return f(lambda a, b: a)

def cdr(f):
	return f(lambda a, b: b)

def test_car():
	assert car(cons(3, 4)) == 3

def test_cdr():
	assert cdr(cons(3, 4)) == 4
