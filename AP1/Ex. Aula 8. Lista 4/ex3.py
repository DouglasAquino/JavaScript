listaNum = []
soma = 0
num = int(input('Numeros: '))
while num >= 0:
    listaNum.append(num)
    num = int(input('Numeros: '))
i = len(listaNum) - 1
while i >= 0:
    print(listaNum[i])
    soma = soma + listaNum[i]
    i = i - 1
print('Soma: ', soma)
