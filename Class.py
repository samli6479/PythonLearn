''' class <name>:
        <suite>  

Assignments & def in <suite> create attributes of the class'''

# Object Construction 

# Idea: All bank accounts have a balance and an account holder

# The account class should add those attributes to each of its instances

''' When a class is called:
    
    1. New instance of the class is created

    2. The __init__ method of the class is called with the new object as its first argument 
       name: self, along with any additional arguments provided.

    3. The __init__ will be called automatically when new instance is created

    4. __init__ is called constructor'''

# Objec Identity that has unique identity

# Identity operator test if two instances are equal

# Biding an object to a new name does not create a new object

# method are functions defined in the suite of a class statement

# self should always be bound to an instance of the Account class

# Invoking method - have access to the object via the self parameter

#                 - they can also access and manipulate the object's state

# Dot notation automatically supplies the first argument to a method

''' Dot notation accesses attributes of the instance or its class

    <expression>.<name>  <expression> Valid Python expression 
                         <name> must be name within the class'''

# Attributes - named information of the objects

# Class attributes are "shared" accros all instances of the class, attributes of class not instances

class Account:
      """An account has a balance and holder.
        All accounts share a common interest rate."""

      interest = 0.02 # A class attribute
        
      def __init__(self, account_holder):
          self.balance = 0
          self.holder = account_holder

      def deposit(self, amount):
          '''Add amount to balance'''
          self.balance = self.balance + amount
          return self.balance

      def withdraw(self, amount):
          '''Substract amount from balance if possible.'''
          if amount > self.balance:
             return 'Insufficient funds'
          self.balance = self.balance - amount
          return self.balance

Jim_Account = Account('Jim')

Edward_Account = Account('Edward')

# Object + Function = Bound Method

type(Account.deposit)  # it is a function

type(Jim_Account.deposit) # it is a method
 
# A function: all arguments within parentheses

# Method: Buildin with its object

''' Assignment to Attributes
    
    1. If the object is an instance, then assignment sets an instance attribute.
   
    2. If the object is a class, then assignment sets a class attribute.'''

Jim_Account.interest = 0.08

Account.interest = 0.04

Edward_Account.interest
