#!/usr/bin/env python

# See http://bit.ly/1gNdaNW

def fibr(n):
    '''Return first n Fibonacci numbers using recursion.'''
    if n <= 1:
        return n
    else:
        return fibr(n - 1) + fibr(n - 2)

def fibg(n):
    '''Return first n Fibonacci numbers using a Python generator'''
    a, b = 0, 1
    for i in xrange(n):
        yield a
        a, b = b, a + b

def fib_rec(n):
    '''Use recursion to generate Fibonacci sequence.'''
    for i in range(n):
        print fibr(i)

def fib_gen(n):
    '''Use Python generator to generate Fibonacci sequence.'''
    print list(fibg(10))

def main():
    '''Main'''
    fib_rec(10)
    fib_gen(10)

if __name__ == "__main__":
    main()
