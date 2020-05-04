nomes = []
populacoes = []
superficies = []
densidades = []
maior = 0
for i in range(3):
    nomes.append(input('Nome: '))
    populacoes.append(int(input('Populações: ')))
    superficies.append(float(input('Superficie: ')))
    densidades.append(populacoes[i]/superficies[i])
    if maior < densidades[i]:
        maior = densidades[i]
print('Densidaded: ', densidades)
print('Maior densidade: ', maior)
for i in range(3):
    if densidades[i] == maior:
        print('Codigo: ', i, '\nNome: ', nomes[i])
