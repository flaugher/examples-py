#!/usr/bin/env python

def palindrome(n):
    '''Check if input number is a palindrome'''
    return str(n) == str(n)[::-1]

def main(n):
    if type(n) is int:
        if palindrome(n):
            print '%s is a palindrome' % n
        else:
            print '%s is not a palindrome' % n
    else:
        raise TypeError('%s is not an Integer' % n)

if __name__ == '__main__':
    main(12321)
    main(12322)
    main('12321')