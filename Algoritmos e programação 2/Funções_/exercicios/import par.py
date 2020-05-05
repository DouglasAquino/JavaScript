'''3.Faça uma função que recebe um valor inteiro e retorna uma mensagem
que informa se o valor é par ou ímpar. '''

from par import *

num = int(input('Digite um numero: '))
if valor(num) == True:
     print('O numero', num, 'é par!')
else:
     print('O numero', num, 'é ímpar!')
