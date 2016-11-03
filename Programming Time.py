# The Consumption of Time

# Problem: how many factors does a postive integer n have?

# Slow: Test each k from 1 through n

# Fast: Test each k from 1 to square root n. For every k, n/k is also a factor

# Time: Slow n Fast Greatest integer less than sqrt(n)


def count(f):
    def counted(*arg):
        counted.call_count += 1
        return f(*arg)
    counted.call_count = 0
    return counted


def divides(k, n):
    return n % k == 0

def factors_slow(n):
    total = 0
    for k in range(1, n+1):
        if divides(k,n):
           total += 1
    return total

from math import sqrt

def factors_fast(n):
    sqrt_n = sqrt(n)
    k ,total = 1,0
    while k <sqrt_n:
          if divides(k, n):
             total += 2
          k += 1
    if k*k == n:
       total += 1
    return total

#divides = count(divides)

#factors_fast(21)

#divides.call_count
