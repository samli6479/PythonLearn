def square(n):
    return n*n

def exp(b, n):                        # Time Theata(n)      Space Theata(n)
    if n == 0:
       return 1                       # Linear and require trember all the n
    else:
       return b * exp(b, n-1)

def fast_exp(b, n):                  # Time Theata(n)       Space Theata(n)
    if n == 0:
       return 1
    elif n % 2 == 0:
       return square(fast_exp(b, n//2))
    else:
       return b * fast_exp(b, n-1)

'''Properties of Orders of Growth

Constant: Constant terms do not affect the order of growth  Theata(n)

Logarithms: The base of logarithm does not affect the order of growth of a process

Nesting: If inner is repeated for every outer, multiply them 

Low-order terms: The fastest-growing part of the computation'''

#Theata(b^n) Exponential Growth Increase Problem Scale by a factor 

#Theata(n^2) Quadratic growth Incrementing n increases problem Scase by n

#Linear Growth Theata(n) #Square root growth # Logarithmic Growth Theata(log n)

#Constant Theata(1) The problem size doesn't matter

