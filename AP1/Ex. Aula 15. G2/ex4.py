'''As informações dos funcionarios do TRE que viajaram a serviço nas eleições devem ser guardadas em uma lista, sendo que cada linha da lista armazena
os dados para pagamento das diarias dos funcionarios: Nome, Quantidade de dias de viagem e valor da diaria do fuuncionario:
Faça um programa que:
° Leia os dados dos funcionarios e armazene na lista, encerrando a leitura quando o usuarios digitar 'sair' para o nome do funcionario, imprimindo a lista
após o preenchimento.
°Crie e imprima uma segunda lista preenchida comn o valor a ser pago pelas diarias da viagem de cada um dos funcionarios, considerando que o indice
da lista é o codigo.
° Calcule e apresente:
    ºO valor total que será gasto pelo TRE com pagamento de diarias.
    ºO maior valor pago.
    ºO nome de todos os funcionarios que viajaram por mais de 10 dias.'''
listafun = []

nome = input('Nome: ')
while nome != 'sair':
    lista = []
    lista.append(nome)
    lista.append(int(input('Quantidade de dias: ')))
    lista.append(float(input('Valor da diaria: R$')))
    listafun.append(lista)
    nome = input('Nome: ')
for i in range(len(listafun)):
    print('\nNome: ', listafun[i][0], '\nQuantidade de dias de viagem: ', listafun[i][1], '\nValor da diaria: R$', listafun[i][2])
pago = []
for i in range(len(listafun)):
    pago.append(listafun[i][1] * listafun[i][2])
for i in range(len(listafun)):
    print('\nCódigo: ', i, '-', 'Valor R$', pago[i])
valortotal = 0
maiorvalor = 0
for i in range(len(pago)):
    valortotal = valortotal + pago[i]
    if pago[i] > maiorvalor:
        maiorvalor = pago[i]
print('Valor total: R$', valortotal)
print('O maior valor: R$', maiorvalor)
for i in range(len(listafun)):
    if listafun[i][1] > 10:
        print('O funcionario {} viajou mais que 10 dias!'.format(listafun[i][0]))
