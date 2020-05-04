inicial = int(input('Valor inicial: '))
final = int(input('Valor final: '))
if inicial == final or inicial > final:
    print('Números impossiveis de calcular!')
i = inicial
impar = 1
while i <= final:
    if i % 2 != 0:
        print(i)
        i = i + 1
    else:
        i = i + 1
