idades = []
nomes = []
sexos = []
novaLista = []
idadeMasc = 0
qtMasc = 0
qtFem = 0
i = 0
while i < 20:
    idades.append(int(input('Idade: ')))
    nomes.append(input('Nome: '))
    sexos.append(input('Sexo: '))
    i = i + 1
i = 0
while i < 20:
    print('Código: ', i, '\nIdade: ', idades[i], '\nNomes: ', nomes[i], '\nSexo: ', sexos[i])
    print('*'*40)
    i = i + 1
i = 0
while i < 20:
    if sexos[i] == 'm':
        idadeMasc = idadeMasc + idades[i]
        qtMasc = qtMasc + 1
    else:
        qtFem = qtFem + 1
    if idades[i] < 18:
        novaLista.append(nomes[i])
    i = i + 1
print('Media das idades dos Homens: ', idadeMasc / qtMasc)
print('Percentual de mulheres: ', (qtFem *100) /20)
print('Nova lista: ', novaLista)
