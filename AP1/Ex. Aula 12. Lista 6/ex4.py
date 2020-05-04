vendedores = []
salMim = float(input('Salario minimo: '))
nome = input('Nome: ')
while nome != 'sair':
    lista = []
    lista.append(nome)
    lista.append(input('Classe: '))
    lista.append(int(input('Quantidade de cadeiras de madeira: ')))
    lista.append(int(input('Quantidade de cadeiras de plastico: ')))
    vendedores.append(lista)
    nome = input('Nome: ')
for i in range(len(vendedores)):
    print('\nNome: ', vendedores[i][0], '\nClasse: ', vendedores[i][1], '\nQuantidade de cadeiras de madeira: ', vendedores[i][2], '\nQuantidade de cadeiras de plastico: ', vendedores[i][3])

for i in range(len(vendedores)):
    if vendedores[i][1] == 'A':
        print('\nNome: ', vendedores[i][0], '\nSalario R$:', salMim * 2 + vendedores[i][3] * 10 + vendedores[i][2] * 20)
    if vendedores[i][1] == 'B':
        print('\nNome: ', vendedores[i][0], '\nSalario R$:', salMim  + vendedores[i][3] * 10 + vendedores[i][2] * 20)
    
