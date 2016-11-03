''' Think about the test cases before you write the function

   Have a test cases in mind before development

Develop step by step 
  
   Cannot depend on code that is not tested

Run the function after development and see the results'''

@trace-- trace function decorator 
def triple(x): -- Decorated function
    return 3 * x

# is identical to 

def triple(x):
    return 3 * x

triple = trace(triple)


