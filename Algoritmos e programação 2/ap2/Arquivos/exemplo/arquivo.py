arq = open('arquivo.txt','r')
conteudo = arq.read().split('\n')
arq.close()

arq2 = open('arquivo2.txt','w')
arq2.write('Produtos:\n')
# Tranforma em uma lista de strings
linha = []
for i in conteudo:
     l= i.split(',')
     linha.append(l)
# Transforma os valores numericos em inteiros
for i in linha:
     i[1] = int(i[1])
# Cria uma relacao de produtos
relacao = []
for i in linha:
     relacao.append(i[0])

# Remove os produtos repetidos
def remove(relacao):
     l = []
     for i in relacao:
          if i not in l:
               l.append(i)
     return l
lista = remove(relacao)
# Cria uma lista de lista dos produtos
relacao1 = []
for i in range(len(lista)):
     relacao1.append([lista[i]])
     
# Cria uma nova lista com os produtos e a quantidade
listacompra = []
for i in range(len(relacao1)):
     a = 0
     for cont in range(len(linha)):
          if linha[cont][0] == relacao1[i][0]:
               a = a + linha[cont][1]
     listacompra.append([relacao1[i][0], a])
print(listacompra)
# Adiciona tudo no novo arquivo
for i in listacompra:
     arq2.write(i[0] + ',' + str(i[1]) + '\n')


arq2.close()
          
          
