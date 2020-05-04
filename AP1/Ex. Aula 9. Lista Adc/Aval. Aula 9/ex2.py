classes = []
quantidades = []
i = 0
salarios = []
somaSal = 0
qtMaior = 0
while i < 50:
    classes.append(input('Classe: '))
    quantidades.append(int(input('Quantidade: ')))
    if classes[i] == 'interno':
        salarios.append(1500 + quantidades[i] * 100)
    else:
        salarios.append(200 * quantidades[i])
    somaSal = somaSal + salarios[i]
    i = i + 1
media = somaSal / 50
i = 0
while i < 50:
    if salarios[i] > media:
        qtMaior = qtMaior + 1
    i = i + 1
print('Salario: ', salarios)
print('Média dos salarios R$:', media)
print('Quantidade que recebem mais que a media: ', qtMaior)
