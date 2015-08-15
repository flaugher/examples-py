#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Examples of decorators 

Decorators are ideal for extending the behavior of functions 
that we don't want to modify. 

Also see
https://wiki.python.org/moin/PythonDecoratorLibrary

"""
def my_decorator(f):
    """Decorator that prints comments before and after function."""
    def wrapper(*args, **kwargs):
        print "About to run function %s" % f.__name__
        result = f(*args, **kwargs)
        print "Just ran function %s" % f.__name__
        return result
    return wrapper

@my_decorator
def add(x, y):
    """Add two numbers."""
    return x + y

@my_decorator
def subtract(x, y):
    """Subtract one number from another."""
    return x - y

def do_math():
    print "Sum is %d" % add(1, 1)
    print "Difference is %d" % subtract(2, 1)

def surround_with(surrounding):
    """Returns function that surrounds a word with something."""
    # Bind surrounding to closure the closure 'surround_with_value'
    def surround_with_value(word):
        """Surround a word with a delimiter."""
        # surround_with_value as access to all names bound to the
        # scope in which it is created.
        return '{}{}{}'.format(surrounding, word, surrounding)
    return surround_with_value

def transform_words(content, targets, transform):
    """Return a string based on 'content' but with each occurrence
    of words in 'targets' replaced with the result of applying
    'transform' to it."""
    result = ''
    for word in content.split():
        if word in targets:
            result += ' {}'.format(transform(word))
        else:
            result += ' {}'.format(word)
    return result

def do_transform():
    # Initialize content
    markdown_string = 'My name if Robert and I\'m learning Python'
    markdown_string_italicized = transform_words(markdown_string,
        ['Python', 'Robert'],  # targets
        surround_with('*'))    # transform (closure function)
    print markdown_string_italicized

if __name__ == "__main__":
    do_math()
    do_transform()    
