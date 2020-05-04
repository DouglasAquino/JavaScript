contNum = 0
soma = 0
prod = 1
lista = []
for i in range(20):
    num = int(input('Numero: '))
    if num != 0:
        lista.append(num)
print(lista)
num2 = int(input('Numero para procurar: '))
for i in range(len(lista)):
    if lista[i] == num2:
        contNum = contNum + 1
    elif lista[i] > num2:
        soma = soma + lista[i]
    else:
        prod = prod * lista[i]
print('Quantidade de numeros: ', contNum)
print('Soma: ', soma)
print('Produto: ', prod)
