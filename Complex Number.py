'''
Complex Arithmetic

Number 1+ sqrt(-1)

Rectangular ComplexRI(1,1)

Polar ComplexMA(sqrt(2),pi/4)
'''

# Use c omplex numers to preform computation  whole data values         x.add(y). x.mul(y)

# add complex number                    real and imaginary parts   real, imag, ComplexRI

# multiply complex number              magnitudes and angles    magnitude, angle, COmplexMA 

'''
Data abstruction and class definitions keep types seperate 

Some operations need access to the implementation of two different abstractions

'''

# Type Dispatching Analysis

# Minimal violation of abstraction barriers: we define cross-type functions as necessary

# Extensible: Any new type can exted itself by adding to new cross-type function dictionaries 

# cross-type implementations m types n operations: m*(m-1)*n

import math

from fractions import gcd

def add_complex_and_rational(c,r):
    return ComplexRI(c.real + float(r.numer)/r.denom, c.imag)

def add_rational_and_complex(r,c):
    return add_complex_and_rational(c,r)

def mul_complex_and_rational(c,r):
    r_magnitude,r_angle= r.numer/float(r.denom),0
    if r_magnitude < 0:
       r_magnitude, r_angle = -r_magnitude, math.pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

def mul_rational_and_complex(r,c):
    return mul_complex_and_rational(c,r)

def Rational_to_Complex(r):
    return ComplexRI(r.numer/float(r.denom),0)

class Number:
      ''' A number.'''
      def __add__(self, other):
          if self.type_tag == other.type_tag:
             return self.add(other)
          elif(self.type_tag, other.type_tag) in self.adders:
             return self.cross_apply(other, self.adders)

      def __mul__(self,other):
          if self.type_tag == other.type_tag:
             return self.mul(other)
          elif(self.type_tag, other.type_tag) in self.multiplier:
             return self.cross_apply(other,self.multiplier)
       
      def cross_apply(self,other,cross_fns):
          cross_fn = cross_fns[(self.type_tag,other.type_tag)]
          return cross_fn(self,other)

      adders = {('com','rat'):add_complex_and_rational,
                ('rat','com'):add_rational_and_complex}

      multiplier = {('com','rat'):mul_complex_and_rational,
                    ('rat','com'):mul_rational_and_complex}

class Complex(Number):
   type_tag = 'com'
   def add(self, other):
       return ComplexRI(self.real + other.real, self.imag + other.imag)

   def mul(self, other):
       return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)

class ComplexRI(Complex):
      """ A rectangular representation."""
      def __init__(self,real,imag):
          self.real = real
          self.imag = imag 

      @property
      def magnitude(self):
          return (self.real ** 2 + self.imag ** 2) ** 0.5 #  x ** 2 = x of the power 2
      
      @property
      def angle(self):
          return math.atan2(self.imag,self.real)

      def __repr__(self):
          return 'ComplexRI({0:g}, {1:g})'.format(self.real,self.imag)

class ComplexMA(Complex):
      ''' A polar representation'''
      def __init__(self,magnitude,angle):
          self.magnitude = magnitude
          self.angle = angle
   
      @property
      def real(self):
          return self.magnitude * math.cos(self.angle)

      @property
      def imag(self):
          return self.magnitude * math.sin(self.angle)

      def __repr__(self):
          return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude,self.angle/math.pi)

class Rational(Number):
      ''' A rational number'''
      type_tag = 'rat'
      def __init__(self,numer,denom):
          g = gcd(numer,denom)
          self.numer = numer // g
          self.denom = denom // g

      def __repr__(self):
          return 'Rational({0},{1})'.format(self.numer,self.denom)

      def add(self,other):
          nx, ny = self.numer,other.numer
          dx, dy = self.denom,other.denom
          return Rational(nx * dy + ny * dx, dx * dy)

      def mul(self,other):
          numer = self.numer * other.numer
          denom = self.denom * other.denom
          return Rational(numer, denom)

# Certain names are special because they have built-in behavior


'''
__init__  method invoked automatically when an object is constructed 

__repr__  method invoked to display an object as a string

__add__ , __bool__....'''
      


