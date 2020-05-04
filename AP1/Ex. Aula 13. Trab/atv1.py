relacoes = [ ['Iogurte', 3.25],
             ['Refrigerante',4.75],
             ['Chocolate',2.00],
             ['Pao',0.50],
             ['Margarina',3.50],
             ['Geleia',4.25],
             ['Leite',3.15]]
        

vendas = [['Pao',5],
          ['Margarina',1],
          ['Geleia',2],
          ['Refrigerante',2],
          ['Pao',3],
          ['Leite',2],
          ['Iogurte',6],
          ['Pao',4],
          ['Chocolate',2],
          ['Chocolate',1],
          ['Pao',5],
          ['Leite',2]]

print("Produto - Preço")
for i in range(len(relacoes)):
    print(relacoes[i][0], "-", relacoes[i][1])

print("\n------------------------------\nProduto - Quantidade vendida")
for i in range(len(vendas)):
    print(vendas[i][0], "-", vendas[i][1])


listacompra = []
for i in range(len(relacoes)):
    a = 0
    for cont in range(len(vendas)):
        if vendas[cont][0] == relacoes[i][0]:
            a = a + vendas[cont][1]
    print('\n------------------------------\n')
    print(relacoes[i][0], a)
    listacompra.append([a*relacoes[i][1], a, relacoes[i][0]])
    print('\nNOME DO PRODUTO: ', listacompra[i][2], '\nQUANTIDADES DE PRODUTOS: ', listacompra[i][1], '\nTOTAL VENDIDO: ', listacompra[i][0])
    
                
                
