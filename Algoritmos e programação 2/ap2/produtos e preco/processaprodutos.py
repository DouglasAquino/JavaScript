arq1=open('teste1.txt','r')
lista = arq1.read().split('\n')
arq1.close()
print(lista)


arq2=open('naotem1.txt','w')
arq3=open('tem2.txt','w')

arq2.write('Produtos\n')
arq3.write('Produtos\n')

for i in lista[1:]:
    if i.endswith('*'):
        arq3.write(i[:-1]+'\n')
    else:
        arq2.write(i+'\n')


arq2.close()
arq3.close()
