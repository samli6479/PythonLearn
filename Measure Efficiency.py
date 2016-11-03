# Fibonacci Sequence
def count(f):  # decorator takes a funciton and returns another function
    def counted(*args):
        counted.call_count += 1 #takes in the same arguments and return the same arguements 
        return f(*args)         # with the how many time it has been called
    counted.call_count = 0 #function is a object, object have attributes
    return counted

def fib_v1(n):
    if n == 0:
       return 0
    elif n == 1:
       return 1
    else:
       return fib_v1(n-1)+fib_v1(n-2)

def fib_v2(n):
    if n==0 or n ==1:
       return n
    else:
       return fib_v2(n-1)+fib_v2(n-2)

# Memorization

# Idea Remember the results that have been computed

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
           cache[n] = f(n)
        return cache[n]
    return memoized # same behavior as f

# what get skiiped is the second time called the same structure

# what lies in the cache 
