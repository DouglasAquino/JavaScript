'''8.	Faça uma função que verifique se um valor é perfeito ou não.
Um valor é perfeito quando ele é igual a soma dos seus divisores, exceto ele próprio.
(por exemplo, 6 é perfeito, pois 6 = 1 + 2 + 3, que são seus divisores).
A função deve retornar um valor booleano:
True se é perfeito e False se não for perfeito.
Pesquise na internet por outros números considerados perfeitos e teste sua função.'''

def perfect(num):
     cont = 1
     soma = 0
     while cont < num:
          if num % cont == 0:
               soma += cont
               cont += 1
          else:
               cont += 1
     return soma

def somatorio(num):
     if num == perfect(num):
          return True
     else:
          return False
