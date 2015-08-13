#!/usr/bin/env python

'''List comprehensions'''

squares = [x*x for x in range(1, 11)]
print squares

even_squares = [x*x for x in range(1, 11) if x % 2 == 0]
print even_squares