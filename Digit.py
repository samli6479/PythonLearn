# Recursive FUnction

def split(n):
    assert n >0, 'n has to be postive'
    '''Split postive n into all but its last digit and its last digit'''    

    return n//10, n%10

def sum_digit(n):
    ''' Return the sum of the digits of postive integer n.'''

    if n<10:
     
       return n 

    else: 

       all_but_last,last=split(n)

       return sum_digit(all_but_last)+last

# conditional statement check the base case, evaluated without revursive calls

# Recurisive cases are evaluated with recurisive calls


def fact(n):
    if n == 0:
       return 1
    else:
       return n * fact(n-1)
### Recursion case only need to track 2 names
### n, fact

def fact_iter(n):
    total, k = 1, 1
    while k <= n:
       total, k = total*k, k+1
    return total

### Iteration cases track 4 names
### n, total, k, fact_iter
