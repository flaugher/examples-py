
def is_prime(num):
    '''Determine if a number is prime.'''
    for x in range(2, num):
        if num % x == 0:
            return False;
    return True;

print is_prime(4)