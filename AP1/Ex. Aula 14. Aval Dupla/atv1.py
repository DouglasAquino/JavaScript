produtos = []


for i in range(3):
    novalinha = []
    novalinha.append(input('Nome: '))
    novalinha.append(float(input('Preço de custo: ')))
    novalinha.append(float(input('Preço de venda: ')))
    novalinha.append(novalinha[2] - novalinha[1])
    produtos.append(novalinha)

print('Produto - Lucro')
for i in range(3):
    print(produtos[i][0], '-' , produtos[i][3])
    print('--------------')


