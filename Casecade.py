def cascade_first(n):
    if n < 10:
       print (n)
    else:
       print (n) 
       cascade(n//10)
       print (n) 

def cascade_second(n):
    print (n)
    if n >= 10:
       cascade(n//10)
       print (n)


### first have the base case which you can track in the structure
