# Attributes for internal Use - attribute name starts with _ is not mean to be referenced externally.

class FibIter:
      "An iterator over Fib"
      def __init__(self):
          self._next = 0
          self._addend = 1

      def __next__(self):
          result = self._next
          self._addend,self._next = self._next, self._addend+self._next
          return result

#fib = FibIter()

#[next(fib) for _ in range(10)]

# Enforced is __ people cannot look the attributes unless in class

# A name bound in local frame is not accessible to other environment
def fib_generator():
    yield 0
    previous, current = 0, 1
    while True:
          yield current
          previous, current = current, previous+current

# Singleton Objects

'''
A singleton class is a class that only ever has one instance.

NoneType, the class of None, is a singleton class. None is its only instance.
'''

class empty_iterator;
      def __next__(self):
          raise StopIteration

empty_iterator=empty_iterator()

# Someone re-bind the class name to the instance




