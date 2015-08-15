#!/usr/bin/env python

def factorial(n):
    """Return n!"""
    return 1 if n < 2 else n * factorial(n - 1)

print factorial(5)