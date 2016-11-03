def fib_tree(n):
    if n == 0:
       return 0
    elif n == 1:
       return 1 
    else:
       return fib(n-2) + fib(n-1)

### When executing the function, makes more than one recursive call

### fib(n-2) and fib(n-1) are two different reursive calls

def fib_iter(n):
    pred, curr = 0, 1
    k = 1
    while k < n:
          pred, curr = curr, pred + curr
          k = k + 1
    return curr

### fin_tree have huge run time so for this problem use iter version

### Recursive decomposition: finding simple instances of the problems

### Think if solving simpler version of the problem helps you solve the problem

def count_partitions(n, m):
    if n == 0:
       return 1
    elif n < 0:
       return 0
    elif m == 0:
       return 0
    else:
       with_m = count_partitions(n-m, m)
       without_m = count_partitions(n, m-1)
       return with_m + without_m
