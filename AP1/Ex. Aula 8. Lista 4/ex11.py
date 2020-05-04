lista = []
i = 0
qtPar = 0
menor = 99999999
qtMenor = 0
while i < 10:
    num = int(input('Numero: '))
    lista.append(num)
    if num % 2 == 0:
        qtPar = qtPar + 1
    if num < menor:
        menor = num
    i = i + 1
i = 0
while i < 10:
    if menor == lista[i]:
        qtMenor = qtMenor + 1
    i = i + 1
print('Quantidade de numeros pares: ', qtPar)
print('O menor elemento: ', menor)
print('Quantidade de vezes que o numero menor se repete: ', qtMenor)
