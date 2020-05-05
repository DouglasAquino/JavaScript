arq = open('produtos.txt','r')
lista = arq.read().split('\n')
arq.close()
print(lista)

arq2 = open('tem.txt','w')
arq3 = open('naotem.txt','w')
arq2.write('Produtos\n')
arq3.write('Produtos\n')
for i in lista[1:]: #lista
     if i.endswith('*'): #strings
          arq2.write(i[:-1]+'\n')
     else:
          arq3.write(i+'\n')
arq2.close()
arq3.close()
