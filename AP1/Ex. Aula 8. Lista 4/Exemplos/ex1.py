lista = []
num = int(input('Numero: '))
while num > 0: #Enquanto numero for > 0
    lista.append(num)
    num = int(input('Numero: '))
print(lista)
tam = len(lista) #Cada tamanho da lista
cont = 0
while cont < tam: #Cada um em uma linha
    print(lista[cont])
    cont = cont + 1

cont = 0
print('Elementos pares: ') #Elementos pares
while cont < tam:
    if lista[cont] % 2 == 0:
        print(lista[cont])
    cont = cont + 1
