lista = []
cont = 0
while cont < 10:
    lista.append(int(input('Número: ')))
    cont = cont + 1
cont = 0
while cont < 10:
    print(lista[cont])
    cont = cont + 1
print('Primeiro elemento da lista: ', lista[0])
print('Ultimo elemento: ', lista[9])
num = int(input('Numero para contar: '))
cont = 0
contNum = 0
while cont < 10:
    if lista[cont] == num:
        contNum = contNum + 1
    cont = cont + 1
print('O número {} aparece {} vezes!'.format(num, contNum))
