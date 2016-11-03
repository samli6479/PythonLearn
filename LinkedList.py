# Linked List Structure

'''
3 ,4 ,5

Link instance 
first: 3
rest:      Link instance 
           first: 4 
           rest:      Link instance
                      first: 5
                      rest:      Link.empty

Linked list is a pair: first value and the rest

Link(3, Link(4, Link(5, Link.empty)))
''' 
#   Attributes are passed to __init__

class Link:

      empty = ()
      # isinstance return whether the value is an instance of a class or a subclass
      def __init__(self, first, rest = empty):
          assert rest is Link.empty or isinstance(rest, Link)
          self.first = first 
          self.rest = rest 

      # Build it like a sequence

      def __getitem__(self, i):
          if i == 0:
             return self.first
          else:
             return self.rest[i-1]

      def __repr__(self):
          return 'Link({0}, {1})'.format(self.first,self.rest)

      def __len__(self):
          return 1 + len(self.rest)

      def __str__(self):
          return '{0}, {1}'.format(self.first, self.rest)

def extend_link(s ,t):
    # Resturn a Link with elements of s followed by elements of t
    if s is Link.empty:
       return t
    else:
       return Link(s.first,extend_link(s.rest,t))

def map_link(f,s):
    # Apply a function to each elemet of Linked List
    if s is Link.empty:
       return s
    else:
       return Link(f(s.first),map_link(f,s.rest))

def filter_link(f,s):
    '''Return a Link with elements of s for which f returns true'''
    if s is Link.empty:
       return s
    else:
       filtered = filter_link(f,s.rest)
       if f(s.first):
          return Link(s.first,filtered)
       else:
          return filtered

def join_link(s, separator):
    '''Return a string of all elements in s separated by separator'''
    if s is Link.empty:
       return ""
    elif s.rest is Link.empty:
       return str(s.first)
    else:
       return str(s.first)+separator+join_link(s.rest,separator)

def link_to_list(s):
    if s is Link.empty:
       return []
    else:
       return [s.first]+link_to_list(s.rest)

def sort_link(s):
    if s == []:
       return Link.empty
    else:
       return Link(s[0],sort_link(s[1:len(s)]))
