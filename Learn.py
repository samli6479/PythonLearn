from math import pi,sqrt

def area(r, shape):
    assert r>0, 'A length must be postive'
    return r * r * shape
# Use Assert to check if the input met the condition

def area_square(r):
    """
    >>> area_square(10)
    100
    """
    return area(r,1)

def area_circle(r):
    return area(r,pi)


# use python -m doctest to test the documentation in def statement
