# Abre o arquivo para leitura
arq = open('precos.csv','r')
conteudo_precos = arq.read().replace(',','.').split('\n') 
arq.close()

# adiciona os elementos da lista conteudo_precos na lista lista_precos.
lista_precos = []
for i in conteudo_precos:
     lista_precos.append(i.split(';'))
del lista_precos[0]

# Abre o arquivo para leitura
arq = open('vendas.txt','r')
conteudo_vendas = arq.read().split('\n')
arq.close()


lista_vendas = []
for i in conteudo_vendas:
     lista_vendas.append(i.split(','))
del lista_vendas[0]

arq = open('total.csv','w')

lista_total = []
total = 0
for i in range(len(lista_precos)):
     a = 0
     for j in range(len(lista_vendas)):
          if lista_precos[i][0] == lista_vendas[j][0]:
               a += int(lista_vendas[j][1])
     total += a * float(lista_precos[i][1])
     lista_total.append([lista_precos[i][0], a, lista_precos[i][1], a * float(lista_precos[i][1])])
lista_total.sort()

arq.write('Produto;Quantidade;Valor Unid;Valor Total\n')
for i in lista_total:
     arq.write(i[0] + ';' + str(i[1]) + ';' + i[2] + ';' + str(i[3]) + '\n')
arq.write('Total' + ';' + str(total))
arq.close()

print('Operação Realizada com Sucesso!')
