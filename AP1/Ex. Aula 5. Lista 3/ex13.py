idade = int(input('Idade: '))
maior = 0
menor = 150
while idade >= 0:
    if idade > maior:
        maior = idade

    if idade < menor:
        menor = idade
    idade = int(input('Idade: '))
    
print('Menor idade: ', menor)
print('Maior idade: ', maior)
