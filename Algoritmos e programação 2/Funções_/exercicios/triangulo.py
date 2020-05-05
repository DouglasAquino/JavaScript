'''10.	Faça uma função que recebe 3 valores reais X, Y e Z e que verifica se esses valores podem ser os comprimentos dos lados de um triângulo.
Caso seja um triângulo, deve retornar o tipo que triângulo que os lados formam, caso contrário retorna uma mensagem informando que não é um triângulo. 
Obs: Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita:
o comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos outros dois lados. 
A função deve identificar o tipo de triângulo formado observando as seguintes definições: 
Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
Triângulo Isósceles: os comprimentos de 2 lados são iguais.
Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.'''

def triangulo(x, y, z):
     if x <= 0 or y <= 0 or z <= 0:
          return 'Valor invalido em um dos lados!'
     elif x + y > z and x + z > y and y + z > x:
          if x == y and y == z:
               return'Triangulo Equlátero!'
          elif x == y or x == z or y ==  z:
               return 'Triangulo Isosceles!'
          elif x != y and y != z and x != z:
               return 'Triangulo Escaleno!'
     else:
          return 'Não são lados de um Triangulo!'
     
