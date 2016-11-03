# Objects -- Represent information

# Consist of data and behavior, uses to create abstractions

# Two different names with the same objects, all the names will be affected

# The same object can change in value through the course of computation 

# All names that refer to the same object are affected by a mutation

# Only objects of mutable types can change: lists & dictionaries

# Dictionary are unordered collections of key-value pairs

# Key restrictions: cannot be a list or a dictionary (any mutable type)

# Two keys cannot be equal

# A function can change the value of any object in its scope

def mystery(s):
    s.pop()
    s.pop()

four = [1, 2, 3, 4]

mystery(four)

# Tuples -- sequence but immutable

tuple(1,)

(1,2,3)

# The value of an expression can change due to change in names or objects

# Name change

x = 2

x = 3

# Object mutation

x = [1, 2]

x.append(3)

# an immutable sequence may still be change if it contains a mutable value as an element

s = ([1, 2], 3)

s[0][0] = 4

# Identity

''' <exp0> is <exp1>  True if evalue to the same object'''

# Equality

''' <exp0> == <exp1> True if evaluate to equal values
