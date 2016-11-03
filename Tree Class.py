# A tree have an entry (any value) at its root and a list of branches:

def count(f):  # decorator takes a funciton and returns another function
    def counted(*args):
        counted.call_count += 1 #takes in the same arguments and return the same arguements 
        return f(*args)         # with the how many time it has been called
    counted.call_count = 0 #function is a object, object have attributes
    return counted

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
           cache[n] = f(n)
        return cache[n]
    return memoized # same behavior as f

class Tree:

    def __init__(self, entry, branches = ()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
    

    def __repr__(self):
        if self.branches:
           branches_repr = ", " +repr(self.branches)
        else:
           branches_repr = ""
        return "Tree({0}{1})".format(self.entry,branches_repr)

@memo
def fib_tree(n):
    if n == 0 or n == 1:
       return Tree(n)
    else:
       left = fib_tree(n-2)
       right = fib_tree(n-1)
       return Tree(left.entry + right.entry, (left,right))
    
def hailstone(n):
    'Print the hail_stone sequence and return the length'
    if n == 1:
       return 1
    elif n % 2 == 0:
       return 1 + hailstone(n//2)
    else:
       return 1 + hailstone(3*n+1)

def is_int(x):
    return int(x) == x

def is_odd(n):
    return n % 2 == 1

def hailstone_tree(k, n=1):
    'Return a tree in which the paths from the leaves the root are all possible hailstone  sequence of length k ending in n.'
    if k == 1:
       return Tree(n)
    else:
       branches = []
       greater, less = n*2, (n-1)/3
       branches.append(hailstone_tree(k-1,greater))
       if less > 1 and is_int(less) and is_odd(less):
          branches.append(hailstone_tree(k-1,int(less)))
       return Tree(n,branches)
