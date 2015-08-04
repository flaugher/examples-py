#!/usr/bin/env python
"""Python iterator class"""

class my_iter:
    """Imitates a Python iterator.
    
    Requirements
    - __iter__ method
    - next method
    - Raise StopIteration
    
    """

    def __init__(self, max):
        self.i = 0
        self.max = max

    def __iter__(self):
        """This makes the object iterable."""

        return self  # Returns an iterator

    def next(self):
        """Returns the next value."""

        if self.i < self.max:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration

def main():
    """Main"""
    pass

if __name__ == "__main__":
    main()
