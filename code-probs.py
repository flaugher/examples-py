#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Potential interview code problems"""

def find_missing_number2(array):
    print [n for n in xrange(1, len(array)+1) if n not in array][0]

def find_missing_number1(array):
    """
    
    Given an array containing all numbers from 1 to N with 
    the exception of one print the missing number to the 
    standard output.

    If input is [5, 4, 1, 2] output is 3

    """
    last = len(array) + 1
    for i in xrange(1, last+1):
        if i not in array:
            print i

def compute_active_users(n, b):
    """Compute number of visitors who didn't leave site after 10 seconds.

    n = number of visitors
    b = bounce rate (# visitors who left site in first 10 seconds)

    Round result down to nearest integer.

    """
    assert n <= 1000000, "n is out of range"
    assert b in range(0, 101), "b is out of range"
    # print int(math.floor(n * ((100. - b)/100.)))
    # You don't need math.floor if converting to an integer

def counter():
    """Count even numbers in a list."""

    def is_even(value):
        """Return True if the value is even."""
        return (value % 2) == 0

    def count_occurrences(target_list, predicate):
        """Return the number of times applying the callable *predicate* to
        list element returns True."""
        return sum([1 for e in target_list if predicate(e)])

    my_predicate = is_even
    my_list = [2, 4, 6, 7, 9, 11]
    result = count_occurrences(my_list, my_predicate)
    print result
    print int(n * ((100. - b)/100.))

def main():
    #counter()
    #compute_active_users(835, 17)  # => 693
    array = [3, 2]
    find_missing_number1(array)
    find_missing_number2(array)


if __name__ == "__main__":
    main()
