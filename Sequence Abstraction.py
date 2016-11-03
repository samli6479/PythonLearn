''' Sequence Abstraction

Length -- A sequence has a finite length.

Element Selection -- A sequence has an element corresponding to any non-negative integer '''

def count_while(s, value):
    ''' Return the numer of occurences of value in s'''
    total, index = 0, 0
    while index < len(s):
          if s[index] == value:
             total = total + 1
          index = index + 1
    return total

# for statement

def count_for(s, value):
    total = 0
    for elem in s: #name is bound in the first frame of the current environment
        if elem == value:
           total = total + 1
    return total

''' for <name> in <expression>:
    <suite>

1. Evaluate the header <expression>, which must yield an iterable value

2. For each element in that sequence, in order: 

   A. Bind <name> to that element in the current frame

   B. Execute the <suite>'''

# [x+1 for x in name] list comprehension

exec('curry = lambda f: lambda x: lambda y: f(x, y)')
curry(pow)(2)(4)

# '\n' Line feed character represents a new line
