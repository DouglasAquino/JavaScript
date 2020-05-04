cont = 0
contNormal = 0
maiorAltura = 0
while cont < 10:
    cont = cont + 1
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    nome = input('Nome: ')
    IMC = peso / altura ** 2
    if IMC < 18.5:
        print('Abaixo do peso!')
    elif IMC < 25:
        print('Peso normal!')
        contNormal = contNormal + 1
    elif IMC < 30:
        print('Acima do peso!')
    else:
        print('Obesidade!')
    if maiorAltura < altura:
        maiorAltura = altura
        nomeMaior = nome
print('Quantidade que tem o peso normal: ', contNormal)
print('Nome da mais alta: ', nomeMaior)
