cont = 0
maior = 0
while cont < 5:
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
    cont = cont + 1
print('O maior numero é: ', maior)
