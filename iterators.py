#!/usr/bin/env python


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
    lst = [1, 2, 3, 4]
    ri = rev_iter(lst)
    print ri.next()
    print ri.next()
    print ri.next()
    print ri.next()    

if __name__ == '__main__':
    main()
