lista = []
i = 0
while i < 50:
    lista.append(input('Nome: '))
    i = i + 1
print(lista[len(lista)-1])
nomePesq = input('Cidade para pesquisa: ')
i = 0
vezes = 0
while i < len(lista):
    if nomePesq == lista[i]:
        vezes = vezes + 1
    i = i + 1
if veze > 0:
    print('Quantidade de vezes que o nome da cidade se repete: ', vezes)
else:
    print('Nome da cidade não existe!')
