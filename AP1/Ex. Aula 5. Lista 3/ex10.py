nome = input('Digite seu nome: ')
maiores = 0
while nome != 'sair':
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        print('Maior de idade!')
        maiores = maiores + 1
    else:
        print('Menor de idade!')
    nome = input('Digite seu nome!')
print('Quantidade de maiores de idade: ', maiores)
