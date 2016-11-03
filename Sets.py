'''
Duplicate elements are removed and are unirdered, same as dictionary
'''

example_set = {435524,3131312,12123,1500}

'''Implementing Sets
# Membership testing
# Union
# Intersection  All three return a new sets.
# Adjoin
'''

# Method one Linked list

from LinkedList import *
                                                        # Time order of growth
def empty(s):                                                 # Theata(1)
    return s is Link.empty

def set_contains(s,v):                                  # Time depends on where v appears
    '''Return whether set s contains value v.'''             # Theata(n) v does not appear

    if empty(s):                                              # Theata(1/2n) = Theata(n)
       return False                                            # Appear in uniformly
    elif s.first == v:
       return True
    else:
       return set_contains(s.rest,v)

def adjoin_set(s,v):                              # Since we majority is on set_contains
    if set_contains(s,v):                         # Theata(n)
       return s
    else:
       return Link(v,s)   # Sets are unordered

def intersect_set(set1, set2):         # Theata(n^2) check every elements in set1 and set2
    in_set2 = lambda v: set_contains(set2, v) # Apply to each element
    return filter_link(in_set2,set1)

def union_set(set1, set2):                             # Theata(n^2) same as above
    not_in_set2 = lambda v: not set_contains(set2, v)
    set1_not_set2 = filter_link(not_in_set2, set1)
    return extend_link(set1_not_set2, set2)

# A set is represented by a linked list with uique elements that is ordered from least to greatest

# Use sets to contain values   Unordered collections   

# Implement set operations     Ordered linked list

def intersect_set(set1,set2):
    if empty(set1) or empty(set2):  # Theata(1)
       return Link.empty
    else:
       e1, e2 = set1.first, set2.first                      #Theata(n) Proceed to either
       if e1 == e2:                                         # List one per time
          return Link(e1,intersect_set(set1.rest,set2.rest))
       elif e1 < e2:
          return intersect_set(set1.rest,set2)
       elif e2 < e1:
          return intersect_set(set1,set2.rest)


