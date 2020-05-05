'''def fibonacci(n):                            #linha1
    if (n<=1):                                 #linha2
        return 1                             #linha3
                                      #linha4
    return fibonacci(n-1)+fibonacci(n-2) #linha5

print (fibonacci(5))'''



#fat(5) = 5 x fat(4)
#fat(4) = 4 x fat(3)
#fat(3) = 3 x fat(2)
#fat(2) = 2 x fat(1)
#fat(1) = 1
#fat(0) = 1

def fat(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fat(n-1)
print(fat(5))

#mult(5,4) = 4 + mult(4,4)
#mult(4,4) = 4 + mult(3,4)
#mult(3,4) = 4 + mult(2,4)
#mult(2,4) = 4 + mult(1,4)
#mult(1,4) = 4
#mult(0,4) = 0

def mult(x,y):
   if x == 1:
       return y
   elif x == 0:
       return 0
   else:
        return y+mult(x-1,y)

print(mult(4,6))

#fib(5) = fib(4) + fib(3)
#fib(4) = fib(3) + fib(2)
#fib(3) = fib(2) + fib(1)
#fib(2) = fib(1) + fib(0)
#fib(1) = 1
#fib(0) = 1

def fib(n):
    if n == 1 or n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print("Fibone ==>",fib(5))

def conv(n,y):
    if n<y:
        return str(n)
    else:
        return conv(n//y)+str(n%y)
print(conv(1,8))