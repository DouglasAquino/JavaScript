pessoas = []
for i in range(4):
    novaLinha = []
    novaLinha.append(input('Nome: '))
    novaLinha.append(int(input('Idade: ')))
    novaLinha.append(input('Sexo: '))
    pessoas.append(novaLinha)
soma = 0
for i in range(4):
    print('Nome: ', pessoas[i][0], '\nIdade: ', pessoas[i][1], '\nSexo: ', pessoas[i][2])
    soma = soma + pessoas[i][1]
media = soma/4
print('\nPessoas com idade maior que a média!')
for i in range(4):
    if pessoas[i][1] > media:
        print(pessoas[i][0])
