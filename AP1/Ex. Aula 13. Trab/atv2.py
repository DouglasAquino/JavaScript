lista = []

for i in range(15):
    novalinha = []
    for cont in range(10):
        novalinha.append('L')
    lista.append(novalinha)

opcao = input('Escolha uma opção: ')
while opcao != 'sair':
    if opcao == '1':
        for i in range(len(lista)):
            print(lista[i])
    elif opcao == '2':
        posicaolinha = int(input('Posicao Linha: '))
        posicaocoluna = int(input('Posicao Coluna: '))
        if lista[posicaolinha-1][posicaocoluna-1] == 'L':
            lista[posicaolinha-1][posicaocoluna-1] = 'O'
            print('Compra efetuada com sucesso!')
        else:
            print('Posição ocupada!')
    opcao = input('Escolha uma opção: ')
