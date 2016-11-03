# Order of Growth

# A method for bounding the resources used by a function by the "size" of a problem

# n: size of the problem

# R(n): measurement of some resource used(time or space)

# R(n) = Theata(f(n))

#Theata means that there exist k1 and k2 s.t. k1f(n)<=R(n)<=k2f(n) for all n larger than some minimum m.
from math import sqrt

                                     # Choose k1 =1

def facotr(n):
    sqrt_n = sqrt(n)                 #1  OW   Statement outside while 4 or 5
    k, total = 1, 0                  #1  OW
    while k < sqrt_n:                #1  IW   Statement inside while 3 or 4( include header)
          if divides(k, n):          #1  IW
             total += 2              #1  IW   while statemnt iterations: between sqrt(n)-1 
          k += 1                     #1  IW   and sqrt(n) ex n=48 or n=49 
    if k *k ==n:                     #1  OW   
       total += 1                    #1  OW
    return total                     #1  OW

# Minimum 4+3*(sqrt(n)-1)

# Maximum 5+4*sqrt(n)

# Maximum operations require per statement: some p 

# Assumption: Every statment takes some fixed number of operations to execute

# m= 25 then we choose k2 = 5p

# Growth is sqrt(n)


