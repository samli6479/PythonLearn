#Coercion

# Some types can be converted into other types

'''
def Rational_to_Complex(r)
    return ComplexRI(r.numer/float(r.denom),0)
'''

class Numer:
      coercions = {('rat','com'):rational_to_complex}

      def __add__(self,other):
          x, y = self.coerce(other)
          return x.add(y)

      def coerce(self, other): # we want them to return the two values with same tags
          if self.type_tag == other.type_tag:
             return self, other
          elif (self.type_tag,other.type_tag) in self.coercions:
             return (self.coerce_to(other.type_tag), other)
          elif (other.type_tag,self.type_tag) in self.coercions:
             return (self, other.coerce_to(self.type_tag) )
      
      def coerce_to(self,other_tag):
          coercion_fn = self.coercions[(self.type_tag,other_tag)]
          return coercion_fn(self)




