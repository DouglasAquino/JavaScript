'''1.Faça uma função que recebe como argumento um valor inteiro e positivo e retorna o valor lógico Verdadeiro (True)
caso o valor seja positivo e Falso (False) caso contrário.'''


def valor(a):
     if a > 0:
          return True
     else:
          return False

'''
2.Utilize a função definida no exercício anterior, passe um determinado valor como argumento para ela, e imprima para o usuário, a mensagem
“O valor N informado é positivo” ou a mensagem “O valor N informado é negativo”.


from valor import *

x = int(input('Digite um valor: '))

if valor(x) == True:
     print('O numero digitado é positivo!')
else:
     print('O numero digitado é negativo!')
'''
