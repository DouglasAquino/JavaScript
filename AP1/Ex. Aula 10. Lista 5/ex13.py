TI = int(input('Termo inicial: '))
r = int(input('Razão: '))
n = int(input('Quantidade de termos: '))
num = TI
for cont in range(n):
    print(num)
    num = num + r
