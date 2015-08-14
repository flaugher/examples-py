#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

"""Examples of closures.

Closures can be used to:
- Replace hard-coded constants
- Replace global variables

"""
def make_inc(x):
    """Increment a number by another number."""
    def inc(y):
        # x is "closed" in the definition of inc.
        # When inc is defined, it knows what x is because
        # x was passed to its enclosing function make_inc.
        # Whenever x is called, it will increment whatever
        # is passed to it via "y" by the value of x.
        return y + x
    return inc

def main():
    # This creates a closure function called "inc5" that always
    # increments the number passed to it by 5
    inc5 = make_inc(5)
    print inc5(5)

    # This creates a closure function called "inc10" that always
    # increments the number passed to it by 10
    inc10 = make_inc(10)
    print inc10(5)

if __name__ == "__main__":
    main()
