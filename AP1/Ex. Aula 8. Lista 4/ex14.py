nome = []
idade = []
maiores = []
idad = int(input('Idade: '))
while idad != 0:
    idade.append(idad)
    nome.append(input('Nome: '))
    idad = int(input('Idade: '))
print('Nomes: ', nome)
print('Idades: ', idade)
i = 0
maior = 0
menor = 120
while i < len(idade):
    if idade[i] >= 18:
        maiores.append(nome[i])
    if idade[i] > maior:
        maior = idade[i]
    if idade[i] < menor:
        menor = idade[i]
    i = i + 1
i = 0
codMenor = []
nomeMenor = []
while i < len(idade):
    if idade[i] == menor:
        codMenor.append(i)
        nomeMenor.append(nome[i])
    i = i + 1
print('Maiores de idade: ', maiores)
print('A maior idade: ', maior)
print('A menor idade: ', menor)
print('Os codigos com a menor idade: ', codMenor)
print('Os nomes das pessoas com a menor idade: ', nomeMenor)
