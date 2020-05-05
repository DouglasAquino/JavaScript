'''4.	Faça uma função que recebe as 3 notas de um aluno como argumento e uma letra, que indicará o tipo da média a ser calculada.
Caso a letra seja A, a função deve calcular a média aritmética das notas do aluno,
se for P, deve ser calculada a média ponderada (pesos: 5, 3 e 2 respectivamente). O cálculo da média deve ser retornado pela função.
Na chamada da função, as 3 notas devem ser informadas pelo usuário e as notas podem ser fracionadas (por exemplo, 7.5 ou 8.5). '''

def notas(x, a, b, c):
     if x == 'A':
          # media aritimetica
          media = (a + b + c)/3
          return media
     else:
          # media aritimetica ponderada
          media = (5*a + 3*b + 2*c) / (5 + 3 + 2)
          return media
'''
from media import *

x = input('Digite o tipo de média: ')

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
c = float(input('Digite a terceira nota: '))

print(notas(x, a, b, c))
'''
