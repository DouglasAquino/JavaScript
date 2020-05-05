'''fatorial'''
'''
fat(5) = 5 * fat(4)
fat(4) = 4 * fat(3)
fat(3) = 3 * fat(2)
fat(2) = 2 * fat(1)
fat(1) = 1
fat(0) = 1
'''
def fat(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fat(n-1)
    
print("fatorial -->",fat(4))


'''multiplicação'''

'''
mult(5,4)=4+mult(4,4)
mult(4,4)=4+mult(3,4)
mult(3,4)=4+mult(2,4)
mult(2,4)=4+mult(1,4)
mult(1,4)=4
mult(0,4)=0
'''

def mult(x,y):
    if x == 1:
        return y
    if x == 0:
        return 0
    else:
        return y+mult(x-1,y)
print("multiplicação -->",mult(5,4))

'''fibonate'''
'''
fib(5) = fib(4) + fib(3)
fib(4) = fib(3) + fib(2)
fib(3) = fib(2) + fib(1)
fib(2) = fib(1) + fib(0)
fib(1) = 1
fib(0) = 1
'''

def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print("fibonate -->",fib(6))



''' CConverso de Binario p/Decimal '''

def bin(x):
    if x==1 or x==0:
        return str(x)
    else:
        return bin(x//2)+str(x%2)
    
print("Binario p/Decimal -->",bin(2))

