class Range:

    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __len__(self):
        return max(0,self.end-self.start)
    
    def __getitem__(self,n):
        if self.start + n >= self.end:
           raise IndexError
        return self.start + n

    def __repr__(self):
        return 'Range({0}, {1})'.format(self.start,self.end)

# Iterators
'''
The Iterator Interface
An iterator is an object that can provide the next element of a sequence

__next__ method of an iterator returns the next element

next function invokes the __next__ method on its argument

If there is not next element, then the __next__ method of an iterator should reaise a StopIteration exception
'''

class RangeIter:
      def __init__(self, start,end):
          self.next = start
          self.end = end

      def __next__(self):
          if self.next >= self.end:
             raise StopIteration
          result = self.next
          self.next += 1
          return result

# Iterables and Iterators

# Iterator: Mutable object that tracks a position in a sequence, advancing on __next__

# Iterable: Represents a sequence and returns a new iterator on __iter__

'''
LetterIter is an iterator: LetterIter('a','e')

Letter is iterable: Letters('a','e')   'a' 'b' 'c' 'd'
'''

class Letters:
      def __init__(self, start, end):
          self.start = start
          self.end = end
      
      def __iter__(self):
          return LetterIter(self.start,self.end)

class LetterIter:
      def __init__(self, start, end):
          self.next_letter = start
          self.end = end

      def __next__(self):
          if self.next_letter >= self.end:
             raise StopIteration
          result = self.next_letter
          self.next_letter = chr(ord(result)+1)
          return result

'''
Iterators from BUilt-in Functions

map(func,iterable): Iterate over func(x) for x in iterable

filter(func, iterable): Iterate over x in iterable if func(x) is ture

zip(first_iter,second_iter): Iterate over co-indexed (x,y) pairs

reversed(sequence): Iterate over x in a sequence in reverse order

View the result

list(iterable): Create list containing all x in iterable 

tuple(iterable): Create a tuple

sorted(iterable): Create a sorted list
'''

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2 * x

# m = map(double, range(3,7))

'''
The For Statement

for <name> in <expression>:
    <suite>

Evaluate the header <expression>, which must evaluate to an iterable object

For each element in that sequnece, in order:
      
    A. Bind <name> to that element in the first frame of the current environment

    B. Execute the <suite>
'''

'''
counts = [1,2,3]
for item in counts:
    print (item)

items = counts.__iter__()
try:
    while True:
         item = items.__next__()
         print(item)
except StopIteration:
         pass # Do nothing
'''

'''

Generators and Generator Functions

A generator function is a function that yields values instead of returning them

A normal function returns once; a generator function yields multiple times

A generator is an iterator, created by a generator function

When a generator function is called, it returns a generator that iterates over yields
'''


def letter_generator(next_letter, end):
    while next_letter < end:
          yield next_letter
          next_letter = chr(ord(next_letter)+1)

# s = letter_generator('a','z')

# next(s)

