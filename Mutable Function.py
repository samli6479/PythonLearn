# A function with Behavior That varies Over Time

# A function compound value have a body and a parent frame

# The parent frame contains the balance, the local state of the withdraw function

# Non-Local Assignment & Persistent Local State

# Work for python 3

def make_withdraw(balance):
    """ Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance   # Declare the name "balance" nonlocal at the top of the body
			   # of the function which it is re-assigned
        if amount > balance:
           return 'Insufficient funds'
        balance = balance - amount #Re-bind balance in the first non-local frame in which
			           #it was bound previously
        return balance
    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance
    return withdraw, deposit

# nonlocal <name>

# Effect: future assignments to that name change its pre-existing binding in the first non-local frame of the current environment 

# Alternative 2.7

def make_withdraw(balance):
    """ Return a withdraw function with a starting balance."""
    balance = [balance]
    def withdraw(amount):
        if amount > balance[0]:
           return 'Insufficient funds'
        balance[0] = balance[0] - amount 
        return balance[0]
    def deposit(amount):
        balance[0] = balance[0] + amount
        return balance[0]
    return withdraw, deposit
