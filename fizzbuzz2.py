
def fizzbuzz(n):
    '''An alternate version of Fizzbuzz'''

    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return str(n)

print '\n'.join(fizzbuzz(n) for n in range(1, 101))