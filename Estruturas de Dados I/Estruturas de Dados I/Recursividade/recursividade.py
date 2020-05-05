#Recursividade / Recursão
#fractais
def fat(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fat(n-1)

def mult(x,y):
    if x==0 or y==0:
        return 0
    elif x==1:
        return y
    else:
        return y+mult(x-1,y)

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def rec(n):
    if n<=10:
        return n*2
    else:
        return rec(rec(n/3))

print(rec(27))
