'''9.	Faça uma função que recebe, como argumento, a altura (alt) e o sexo de uma pessoa e retorna o seu peso ideal.
Para homens, calcular o peso idealusando a fórmula peso ideal = 72.7 x alt - 58 e ,para mulheres, peso ideal = 62.1 x alt - 44.7.'''

def peso_ideal(altura, sexo):
     if sexo == 'masculino' or sexo == 'm':
          ideal = 72.7 * altura - 58
          return ideal
     else:
          ideal = 62.1 * altura - 44.7
          return ideal

