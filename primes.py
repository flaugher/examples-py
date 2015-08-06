#!/usr/bin/env python

def is_prime(num):
    '''Determine if a number is prime.'''
    for x in range(2, num):
        if num % x == 0:
            # return False
            print "%s is not a prime number" % num
    # return True
    print "%s is a prime number" % num

def main():
    '''Main'''
    is_prime(5)

if __name__ == "__main__":
    main()