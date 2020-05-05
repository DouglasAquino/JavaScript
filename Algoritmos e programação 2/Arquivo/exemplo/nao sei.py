relacoes = [['iorgute'],
            ['refrigerante'],
            ['chocolate']]

vendas = [['iorgute', 3],
          ['refrigerante', 2],
          ['chocolate', 1],
          ['iorgute', 1],
          ['chocolate', 6]]

lista = []
for i in range(len(relacoes)):
     a = 0
     for cont in range(len(vendas)):
          if vendas[cont][0] == relacoes[i][0]:
               a += vendas[cont][1]

     lista.append([a, relacoes[i][0]])

print(lista)
