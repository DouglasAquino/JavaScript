from nomes import*


nome1 = input('Digite os nomes: ')
nome2 = input('Digite os nomes: ')
nome3 = input('Digite os nomes: ')


print(maioresNomes(nome1, nome2, nome3))


from random import randint

numeros = []
for i in range(10):
     numeros.append(randint(1, 100))
     
print(imprimePares(numeros))
