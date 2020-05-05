# Lista Preço
arq = open('precos.csv','r')
conteudo = arq.read().split('\n')
arq.close()

linha =[]
for i in conteudo:
    l = i.split(';')
    l[1] = l[1].replace(',','.')
    linha.append(l)
del linha[0]
for i in linha:
    i[1] = float(i[1])
relacao_produtos = []
for i in linha:
    relacao_produtos.append(i)
relacao_produtos.sort()

# Segunda Lista 'Vendas'
arq = open('vendas.txt','r')
vendas = arq.read().split('\n')
arq.close()
lista_vendas= []
for i in vendas:
    l = i.split(',')
    lista_vendas.append(l)
del lista_vendas[0]
for i in lista_vendas:
    i[1] = int(i[1])

# Total 
soma = 0
listacompra = []
for i in range(len(relacao_produtos)):
     a = 0
     for cont in range(len(lista_vendas)):
          if lista_vendas[cont][0] == relacao_produtos[i][0]:
               a = a + lista_vendas[cont][1]
     soma += a * relacao_produtos[i][1]
     listacompra.append([relacao_produtos[i][0], a, relacao_produtos[i][1], a*relacao_produtos[i][1]])

# Adicionar no novo arquivo
arq2 = open('total.csv','w')
arq2.write('Produto;Quant;Valor Unid;Valor Total\n')
for i in listacompra:
    arq2.write(i[0] +','+ str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + '\n')
arq2.write('Total' + ';')
arq2.write(str(soma))
arq2.close()
print('Operação realizada com sucesso!')

