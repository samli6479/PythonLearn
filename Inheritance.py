# Inheritance

# Common use: a specialized class inherits from a more gneral class

# class<new class>(<base class>):

# New class shares the attributes with the base class.

# Checking accounts - interest rate of 0.01

#                   - withdraw fee of 1


'''
   1. Use existing implementations 

   2. Reuse overridden attributes by accessing through the base class

   3. Look up attributes on instances

'''

'''
Inheritance: Relating through specifying similarities and differences- is a relationship

Composition: Connecting two classes through their relationship to one another - has a 

'''

class Account:
      """ A bank account"""
      interest = 0.02

      def __init__(self, account_holder):
          self.balance = 0
          self.holder = account_holder
 
      def deposit(self, amount):
          self.balance = amount + self.balance
          return self.balance

      def withdraw(self, amount):
          if amount > self.balance: 
             return 'Insufficient Fund'
          self.balance = self.balance - amount
          return self.balance

class CheckingAccount(Account):
      """ A Checking account"""

      interest = 0.01 # overriding
      
      withdraw_fee = 1

      def withdraw(self, amount):
          return Account.withdraw(self, amount + self.withdraw_fee)

class SavingAccount(Account):
      """ A Saving account """
      
      deposit_fee = 2 

      def deposit(self,amount):
          return Account.deposit(self,amount - self.deposit_fee)

''' Python 3
class BestAccount(CheckingAccount, SavingAccount):
      def __init__(self, account_holder):
          self.holder = account_holder
          self.balance = 100
'''


class BestAccount(CheckingAccount, SavingAccount):
      def __init__(self, account_holder):
          self.holder = account_holder
          self.balance = 100
      
      def deposit(self,amount):
          return SavingAccount.deposit(self, amount)

class Bank: 
      """ A bank has accounts and pay interest """

      def __init__(self):
          self.accounts = []   # composition - the bank has the accounts
 
      def open_account(self, holder, amount, account_type= Account):
          account = account_type(holder)
          account.deposit(amount)
          self.accounts.append(account)
          return account

      def pay_interest(self):
          for account in self.accounts:
              account.deposit(account.balance * account.interest)

CIBC = Bank()
          
John_Best = CIBC.open_account("John",1000,BestAccount)
          
John_Best.deposit(100)

John_Best.withdraw(50)

John_Best.interest


      
      

