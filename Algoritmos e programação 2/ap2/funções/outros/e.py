'''def contador(i,f,p):
     
     c = i
     while c <= f:
          print(f'{c}', end='..')
          c += p
     print('Fim')

contador(2,10,2)
'''
'''
def soma(a=0,b=0,c=0):
     s = a + b + c
     print('Soma: ', s)

soma(3,2,5)
'''
'''
def teste(b):
     b += 4
     c = 2
     print(a)
     print(b)
     print(c)
a = 5
teste(a)
'''
'''
def somar(a=0, b=0, c=0):
     s = a + b + c
     return s

print(somar(3, 2, 5))
'''
'''
def fatorial(num = 1):
     f = 1
     for c in range(num, 0, -1):
          f *= c
     return f
n = int(input('Digite um numero: '))
print(fatorial(n))
'''
'''
def par(n = 0):
     if n %2 == 0:
          return True
     else:
          return False

num = int(input('Digite um numero: '))

if par(num):
     print('É par!')
else:
     print('Não é par!')

'''

# Questao 1
def positivo(num):
     if num >= 0:
          return True
     else:
          return False
num = int(input('Digite o número: '))

if positivo(num):
     print(num, 'é positivo!')
else:
     print(num, 'não é positivo!')










