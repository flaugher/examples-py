#!/usr/bin/env python

"""Examples of Python generators"""

def counter_generator(first, last):
    """Generator that returns a counter."""
    print "Inside the counter generator"
    current = first
    while current <= last:
        yield current
        current += 1

def run_counter():
    """Run the counter generator."""
    for i in counter_generator(1, 5):
        print i

def simple_generator():
    """Generate characters 'a' through 'c'."""
    print "Inside the simple generator"
    yield 'a'
    yield 'b'
    yield 'c'

def run_simple():
    """Run the simple generator."""
    # Generators are a form of iterator so we can use them as such
    for c in simple_generator():
        print c

def main():
    """Main"""
    run_simple()
    run_counter()

if __name__ == "__main__":
    main()
