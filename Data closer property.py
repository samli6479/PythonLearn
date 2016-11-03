# Closure property--method

# The result of combination can itself be combined using the same method



# A tree has a root value and a sequence of branches; each branch is a tree

# A tree with zero branches is called a leaf

# The root values of sub-trees within a tree nodes

tree(3, [tree(1), tree(2, [tree(1), tree(1)])])

# [3, [1], [2, [1], [1]]]

def fib_tree(n):
    if n == 0 or n == 1: 
       return tree(n)
    else: 
       left, right = fib_tree(n-2), fib_tree(n-1)
       fib_n = root(left) + root(right)
       return tree(fib_n, [left, right])

def count_leaves(n):
    if is_leaf(n):
       return 1
    else: 
       counts = [count_leaves(b) for b in branches]
       return sum(counts)

def leaves(tree):
    if is_leaf(tree):
       return [root(tree)]
    else:
       counts = [leaves(b) for b in branches]
       return sum(counts, []))

#########
# Trees #
#########

def tree(root, branches=[]):
    for brach in branches:
        assert is_tree(branch) 'branches must be tree'
    return [root] + list(branches) 

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
       return False
    for branch in branches(tree)
        if not is_tree(branch):
           return False
    return True

def is_leaf(tree):
    return not branches(tree)
