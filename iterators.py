#!/usr/bin/env python

class Counter:
    """Return numbers between two numbers (inclusive)."""
    def __init__(self, first, last):
        """Initialize counter."""
        self.current = first
        self.last = last

    def __iter__(self):
        """Return self as an iterator instance."""
        return self

    def next(self):   # __next__ in Python 3!
        """Return next number."""
        if self.current <= self.last:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

class fwd_iter():
    """Iterate over a list"""

    def __init__(self, lst):
        self.i = lst[0]
        self.max = lst[-1]

    def __iter__(self):
        return self

    def next(self):
        if self.i <= self.max:
            # Return current value
            i = self.i
            # Increment value for next interation
            self.i += 1
            return i
        else:
            raise StopIteration()

class rev_iter():
    """Iterate over list in the reverse direction"""

    def __init__(self, lst):
        self.i = lst[-1]
        self.min = lst[0]

    def __iter__(self):
        return self

    def next(self):
        if self.i >= self.min:
            i = self.i
            self.i -= 1
            return i
        else:
            raise StopIteration()

def main():
    print "Running reverse iterator"
    lst = [1, 2, 3, 4]
    ri = rev_iter(lst)
    print ri.next()
    print ri.next()
    print ri.next()
    print ri.next()

    print "Running Counter iterator"
    c = Counter(1, 5)
    for i in c:
        print "%s " % i

if __name__ == '__main__':
    main()
