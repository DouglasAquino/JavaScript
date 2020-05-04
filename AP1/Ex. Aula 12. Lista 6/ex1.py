lista = []
media = 0
for i in range(100):
    nova = []
    nova.append(input('Nome: '))
    nova.append(int(input('Idade: ')))
    lista.append(nova)
    media = media + lista[i][1]
smed = media / 100
for i in range(len(lista)):
    print('Nome: ', lista[i][0], '\nIdade: ', lista[i][1])
for i in range(len(lista)):
    if lista[i][1] > smed:
        print('Nome dos maiores que a media: ', lista[i][0])
pesq = input('Nome para pesquisa: ')
entrou = 'nao'
for i in range(len(lista)):
    if lista[i][0] == pesq:
        print('Idade: ', pessoas[i][1])
        entrou = 'sim'
if entrou == 'nao':
    print('Não tem na lista!')
