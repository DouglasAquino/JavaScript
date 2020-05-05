def fatorial(n):
    if n == 0 or n == 1: #base da recursão
        return 1
    
    else:
        return n * fatorial(n-1) #chamada recusiva

def mult(x,y):
    if y == 0 or x == 1:
        return 0
    
    elif x == 1:
        return y

    else:
        return y + mult(x-1,y)

def fibonacci(n):
    if n == 1 or n == 2: #base da recursão
        return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2) #chamada recusiva


    
