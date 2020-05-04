mediaSal = 0
maiorSal = 0
menorSal = 999999
cont = 0
nome = input('Nome: ')
while nome != 'fim':
    salario = float(input('Salario do funcionario: '))
    cont = cont + 1
    mediaSal = mediaSal + salario
    if maiorSal < salario:
        maiorSal = salario
    elif salario < menorSal:
        menorSal = salario
    nome = input('Nome: ')
print('Media Salarial: ', mediaSal / cont)
print('Maior Salario: ', maiorSal)
print('Menor Salario: ', menorSal)
