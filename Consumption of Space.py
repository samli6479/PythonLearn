# Which environment frames do we need to keep during evaluation?

# There is a set of active environments Values and frames in active environments consume memory

# Memory that is used for other values and frames can be recycled

# Active environments:
  # Environments for any functions calls currently being evaluated 
  # Parent environments of functions named in active environments
  # Functions returned can be reused
  # max length of active frames at any given time determines how many memory we need

def count_frames(f):
    def counted(*arg):
        counted.open_count += 1
        if counted.max_count < counted.open_count:
           counted.max_count = counted.open_count
        result = f(*arg)        
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

@count_frames
def fib(n):
    if n ==0 or n ==1:
       return n
    else:
       return fib(n-2) + fib(n-1)
