import numpy as np

print('hello Clemence')
print(np.cos(0))

def add(a, b):
    return a+b

def div(a, b):
    if b == 0:
        if a > 0:
            return float("inf")
        elif a < 0:
            return float("-inf")
        else:
            raise ArithmeticError("Can't divide 0 by 0")
            
    return a/b

def sub(a, b):
    return a - b
