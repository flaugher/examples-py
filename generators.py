#!/usr/bin/env python

"""Examples of Python generators

Generators are good for performing "lazy" evaluations
when you're working with lots of data.  Generators 
eliminate the need save all the generated data in 
memory all at once.  The generator will "generate"
and return one piece of data at a time.

Note that these generators are not reusable.

"""
def generator_expression():
    """Generate squares of a list of numbers."""
    print "Running list expression"
    print [x*x for x in range(1, 5)]

    print "Running a generator expression"
    # Generator expressions are like list expressions except
    # that they're enclosed in round brackets instead of square ones
    ge = (x*x for x in range(1, 5))
    for i in ge:
        print i

def infinite_generator(start=1):
    """Generate an infinite set of numbers."""
    while True:
        yield start
        start += 1

def counter_generator(first, last):
    """Generator that returns a counter."""
    print "Inside the counter generator"
    current = first
    while current <= last:
        # Return ("yield") current value, increment current,
        # and suspend state until next iteration
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
    generator_expression()

if __name__ == "__main__":
    main()
