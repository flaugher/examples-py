#!/usr/bin/env python

def fizzbuzz():
    '''Print numbers from 1 to 100 with some exceptions.

    A perenial favorite!

    - If number is a multiple of 3, print "fizz" instead of number
    - If number is a multiple of 5, print "buzz" instead of number
    - If number is multiple of both 3 and 5, print "fizzbuzz" instead
    of the number.

    '''
def fizzbuzz(n):
    assert n > 0, "n is less than lower bound %d" % 1
    assert n <= 1000, "n exceeds upper bound %d" % 1000

    for i in range(1, n+1):
        if i % 15 == 0:
            print "Fizzbuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i

def main():
    '''Main'''
    fizzbuzz(25)

if __name__ == "__main__":
    main()