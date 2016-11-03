'''
Functional Programming

All functions are pure functions

No re-assignment and no mutable data types 

Name-value binds are permanent

Advantages:

    The value of an expression is independent of the order of aub-expressions

    Sub-expressions can evaluated in parallel or only on demand

    Referential transparency: The value of an expression does not change when we sub one of its sub expression with the value of that subexpression

But no for/while statements!

Recursion and Iteration in Python
'''

def factorial(n,k):         # Recursion               Time        Space
    'Computes; n!*k'                                # Theata(n)   Theata(n)
    if n == 0:
       return k
    else:
       return factorial(n-1,k*n)
 
def factorial(n,k):         # Iteration             Theata(n)     Theata(1)
    while n > 0:
          n, k = n-1, k*n
    return k

# Tail Recursion  Eliminate the middle man

