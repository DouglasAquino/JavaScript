nomes = []
populacao = []
superficie = []
densidade = []
maior = 0
for i in range(10):
    nomes.append(input('Nome: '))
    populacao.append(int(input('População: ')))
    superficie.append(float(input('Superficie: ')))
    densidade.append(populacao[i] / superficie[i])
    if maior < densidade[i]:
        maior = densidade[i]
print('Densidade: ', densidade)
print('Maior densidade: ', maior)
for i in range(10):
    if densidade[i] == maior:
        print('Codigo: ', i, 'Nome: ', nomes[i])
