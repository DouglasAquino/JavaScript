nome = []
trabalho = []
notaProva = []
notaFinal = []
i = 0
while i < 5:
    nome.append(input('Nome: '))
    trabalho.append(input('Fez o trabalhgo: '))
    notaProva.append(float(input('Nota da prova: ')))
    i = i + 1
i = 0
while i < 5:
    if trabalho[i] == 'sim':
        notaFinal.append(notaProva[i] + 1)
    else:
        notaFinal.append(notaProva[i])
    i = i + 1
i = 0
somaMedia = 0
media = 0
while i < 5:
    somaMedia = somaMedia + notaFinal[i]
    i = i + 1
media = somaMedia / len(nome)
i = 0
cod = []
nom = []
while i < 5:
    if notaFinal[i] < media:
        cod.append(i)
        nom.append(nome[i])
    i = i + 1
print('Nomes: ', nome)
print('Notas Finais: ', notaFinal)
print('Média das Notas: ', media)
print('Código dos abaixo da media: ', cod)
print('Nome dos abaixo da media: ', nom)
