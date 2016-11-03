# Message Passing: Objects interact by looking up attributes on each other 

# A shared message that act similar behavior from different type of objects 

# An interface is a set of shared attributes that act the same things for different classes

# repr only looks from class

"""
def repr(o):
    return type(o).__repr__(o)

def str(o):
    if hasattr(type(o),'__str__'):
       return type(o).__str__(o)
    else:
       return repr(o)
"""
'''
Property Method - allows to update attributes automatically

Allow zero-argument methods to be called without expression
'''

class Rational:
      def __init__(self, n, d):
          self.numer = n
          self.denom = d
      def __repr__(self):
          return 'Rational({0},{1})'.format(self.numer,self.denom)
      def __str__(self):
          return '{0}/{1}'.format(self.numer,self.denom)
      @property
      def float_value(self):
          return float(self.numer) / self.denom
