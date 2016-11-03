''' Assume we can compose rational numbers:
    ratonal(n,d) returns a rational number x --- Constructor
    numer(x) returns the numerator of x   }
    denom(x) returns the denominator of x }   Selectors'''

pair = [1,2]  # A list literal: Comma-seperated expressions in brackets

from fractions import gcd

def rational(n, d):
    ''' Construct a rational number that represents N/D.'''
    g=gcd(n,d)
    return [n // g, d // g]

def numer(x):
    ''' Return the numerator of rational number x.'''
    return x[0]

def denom(x):
    ''' Return the denominator of rational number x.'''
    return x[1]

def add_rational(x, y):
    ''' Add rational numbers x and y.'''
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    ''' Multiply rational numbers x and y.'''
    return rational(numer(x)*numer(y),denom(x)*denom(y))

def rationals_are_equal(x, y):
    ''' Return whether the two rationals are equal.'''
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    '''Print rational number'''
    print str(numer(x)) + " / " + str(denom(x))
