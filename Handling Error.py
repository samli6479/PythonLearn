'''
Sometimes, computer programs behave in non-standard ways
- A function receives an argument value of an improper type
- Some resoure is not avaliable
- A network connection is lost during data transmission'''

# Exceptions

# a built-in mechanism in a language to declare and respond to exceptional conditions 

# Python raises an exception whenever an error occurs. 

# Exceptions can be handled by the program, preventing the interpreter from halting.

# Unhandled exceptions will cause Python to halt execution and print a stack trace. 

''' Matering exceptions:
Exceptions are objects!
Enable non-local conuations of control'''

# Assert Statements

# assert <expression>, <string>

''' Python3 -O to disregard assertion'''

# Raise statements 

''' raise <expression>
<expression> must evaluate to a subclass of BaseException or an instance of one'''

# TypeError -- A function was passed the wrong number/type of argument

# NameError -- A name wasn't found

# KeyError -- A key wasn't found in a dictionary

# RuntimeError -- Catch-all for troubles during interpretation

# Try statement

'''
try:
   <try suite>
except <exception class> as <name>:
   <except suite>
'''
# Try first then if exception raised, the class of exception inherits from exception class then expcetion suite executed, with <name> bound to the exception

try:
    x = 1/0
except ZeroDivisionError as e:
    print ('Handling a', type(e))
    x = 0

# Multiple try statements: Jumps tp the except suite of the most recent try statement that handles that type of exception

def invert(x):
    result = 1/x
    print('Never will be printed if x is 0')
    return result

def invert_safe(x):
    try:
       return invert(x)
    except ZeroDivisionError as e:
       return str(e)

# Try statement only evaluate the error while function

