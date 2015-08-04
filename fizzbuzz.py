#!/usr/bin/env python

def fizzbuzz():
    '''Print numbers from 1 to 100 with some exceptions.

    A perenial favorite!

    - If number is a multiple of 3, print "fizz" instead of number
    - If number is a multiple of 5, print "buzz" instead of number
    - If number is multiple of both 3 and 5, print "fizzbuzz" instead
    of the number.

    '''
    for n in range(1, 101):
        if n % 3 == 0:
            output = "fizz"
            if n % 5 == 0:
                output += "buzz"
        elif n % 5 == 0:
            output = "buzz"
            if n % 3 == 0:
                output = "fizz" + output
        else:
            output = n
        print output

def main():
    '''Main'''
    fizzbuzz()

if __name__ == "__main__":
    main()