import random
numeros = []
i = 0
for i in range(50):
    numeros.append(random.randint(1, 100))
print('Numeros: ', numeros)
medsoma = 0
for i in range(50):
    if i < 25:
        medsoma = medsoma + numeros[i]
media = medsoma / 25
print('Média dos 25 primeiros elementos: ', media)
somaposi = 0
for i in range(50):
    if numeros[i] >= 0:
        somaposi = somaposi + numeros[i]
print('Soma dos positivos: ', somaposi)
qtvez = 0
for i in range(50):
    if numeros[i] == numeros[49]:
        qtvez = qtvez + 1
print('Qt. que o ultimo elemento aparece: ', qtvez)
for i in range(50):
    if i == 0:
        print('Não tem antecessor: ', 'Numero: ', numeros[i], 'Sucessor: ', numeros[i + 1])
    elif i == 49:
        print('Antecessor: ', numeros[i - 1], 'Numero: ', numeros[i], 'Não tem sucessor!')
    else:
        print('Antecessor: ', numeros[i - 1], 'Numero: ', numeros[i], 'sucessor: ', numeros[i + 1] )
