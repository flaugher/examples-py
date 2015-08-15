#!/usr/bin/env python
# -*- coding: utf-8 -*-

def make_adder(num):
    def add_to(n):
        return num + n
    return add_to

def call_make_adder():
    print "Calling make_adder"
    add10 = make_adder(10)
    print add10(1)  # => 11

def make_power(n):
    """Define a closure that raises a number to the power of n."""
    def nth_power(x):
        return x**n
    return nth_power

def call_make_power():
    print "Calling make_power"
    squared = make_power(2)
    print squared(2)
    cubed = make_power(3)
    print cubed(2)
    # Note that you could delete make_power from the namespace
    # at this point and the squared and cubed closures would 
    # still work!

def make_inc(x):
    """Increment a number by another number.

    The call to makeInc creates a binding for x that is
    referenced inside the function inc. Each call to makeInc 
    creates a new instance of this function, but each instance 
    has a link to a different binding of x.

    """
    def inc(y):
        # x is "closed" in the definition of inc.
        # When inc is defined, it knows what x is because
        # x was passed to its enclosing function make_inc.
        # Whenever x is called, inc will increment whatever
        # is passed to it via "y" by the value of x.
        return y + x
    return inc

def call_make_inc():
    # This creates a closure function called "inc5" that always
    # increments the number passed to it by 5
    print "Calling make_inc"
    inc5 = make_inc(5)
    print inc5(5)

    # This creates a closure function called "inc10" that always
    # increments the number passed to it by 10
    inc10 = make_inc(10)
    print inc10(5)

def main():
    call_make_inc()
    call_make_power()
    call_make_adder()

if __name__ == "__main__":
    main()
