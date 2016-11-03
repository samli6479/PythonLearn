# Curry Transform a multi-agrument function into a single-argument, higher-order function

def curry(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

### example curry(add)(2)(4)=6
