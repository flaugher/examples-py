#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_decorator(f):
    """Decorator that prints comments before and after function."""
    def wrapper(*args, **kwargs):
        print "About to run function"
        result = f(*args, **kwargs)
        print "Just ran function"
        return result
    return wrapper

@my_decorator
def add(x, y):
    """Add two numbers."""
    return x + y

if __name__ == "__main__":
    sum = add(1, 1)
    print sum
