#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_decorator(f):
    """Decorator that prints comments before and after function."""
    def wrapper(*args, **kwargs):
        print "About to run function %s" % f.__name__
        result = f(*args, **kwargs)
        print "Just ran function %s" % f.__name__
        return result
    return wrapper

@my_decorator
def add(x, y):
    """Add two numbers."""
    return x + y

@my_decorator
def subtract(x, y):
    """Subtract one number from another."""
    return x - y

if __name__ == "__main__":
    print "Sum is %d" % add(1, 1)
    print "Difference is %d" % subtract(2, 1)
