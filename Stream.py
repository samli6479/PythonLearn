# Stream are lazy linked list

# A stream is a linked list, but the rest of the list is computed on demand

'''
Link- First element is anything
    - second element is a Link instance or Link.empty

Stream -First element can be anything

       - Second element is a zero-argument function that returns a Stream or Stream.empty

Once Created, the Link and Stream can be used interchangeable 

namely first, rest
'''
class Stream:
      
      class empty:
            def __repr__(self):
                return 'Stream.empty'
      
      empty = empty()

      # Singleton Class
  
      def __init__(self,first,compute_rest = lambda: Stream.empty):
          assert callable(compute_rest), 'compute_rest must be callable.'  # Zero Argument 
          self.first = first
          self._compute_rest = compute_rest

      @property
      def rest(self):
          if self._compute_rest is not None:
             self._rest = self._compute_rest()
             self._compute_rest = None
          return self._rest

      def __repr__(self):
          return 'Stream({0}, <...>)'.format(repr(self.first))


# An integer stream is a stream of consecutive integers

# Start with first. Constructed from first and a function compute_rest that returns the integer stream starting at first+1

def integer_stream(first):           
    def compute_rest():                               
        return integer_stream(first+1)
    return Stream(first,compute_rest)

#   same as

def int_stream(first):
    return Stream(first, lambda: int_stream(first+1))

def first_k(s,k):
    values = []
    while s is not Stream.empty and k>0:
          values.append(s.first)
          s, k = s.rest, k-1
    return values

def square_stream(s):
    first = s.first*s.first
    return Stream(first, lambda: square_stream(s.rest))

def add_stream(s,t):
    first = s.first + t.first
    return Stream(first, lambda: add_stream(s.rest,t.rest))

#same 

def added_stream(s,t):
    first = s.first + t.first
    def compute_rest():
        return added_stream(s.rest,t.rest)
    return Stream(first,compute_rest)
   
ones = Stream(1, lambda: ones)

ints = Stream(1, lambda: add_stream(ones,ints))

# Mapping a function over a stream

'''
Mapping a function over a stream applies a function only to the first element right away,
the rest is computed lazily
'''

def map_stream(fn,s):
    "Map a function fn over the elements of a stream."""
    if s is Stream.empty:
       return s
    def compute_rest():
       return map_stream(fn, s.rest)
    return Stream(fn(s.first),compute_rest)

# Filtering a Stream

# When filtering a stream, processing continues until a element is kept in the output

def filter_stream(fn,s):
    'Filter stream s with predicate function fn.'
    if s is Stream.empty:
       return s
    def compute_rest():
       return filter_stream(fn,s.rest)
    if fn(s.first):
       return Stream(s.first,compute_rest)
    else:
       return compute_rest()

odds = lambda x: x % 2 == 1

odd = filter_stream(odds, ints)

def primes(s):
    ' Return a stream of primes, given a stream of postive integers.'
    def not_divisible(x):
        return x % s.first != 0
    def compute_rest():
        return primes(filter_stream(not_divisible, s.rest))
    return Stream(s.first, compute_rest)

p = primes(int_stream(2))


