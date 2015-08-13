#!/usr/bin/env python
"""Potential interview code problems"""
import pickle

def dump_pickle():
    """Serialize dictionary using pickle."""
    fav_color = {"lion": "yellow", "kitty": "black"}
    pickle.dump(fav_color, open("pickle-file", "wb"))

def load_pickle():
    """De-serialize dictionary using pickle."""
    fav_color = pickle.load(open("pickle-file", "rb"))
    print fav_color

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

def main():
    """Main"""
    #dump_pickle()
    load_pickle()
    #counter()

if __name__ == "__main__":
    main()
