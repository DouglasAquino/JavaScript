'''def fat(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fat(n-1)


d = int(input("Digite o numero: "))
print(fat(d))'''

'''
def mult(x, y):
    if x == 1:
        return y
    elif x == 0 or y == 0:
        return 0
    else:
        return y + mult(x-1, y)

x = int(input("Digite o numero: "))
y = int(input("Digite o numero: "))
print(mult(x, y))


def exp(x, y):
    if x == 0:
        return 0
    elif y == 0 or x == 1:
        return 1
    elif y == 1:
        return x
    else:
        return x * exp(x, y - 1)
        
x = int(input("Digite o numero: "))
y = int(input("Digite o numero: "))
print(exp(x, y))'''


def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n = int(input("Digite o numero: "))
print(fib(n))
















