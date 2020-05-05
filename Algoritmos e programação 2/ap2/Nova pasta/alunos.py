arq = open('alunos.txt','r')
conteudo = arq.read().split('\n')
arq.close()
print(conteudo)

lista = []
for i in conteudo:
     linha = i.split(',')
     lista.append(linha)
#del lista[0]
lista.pop(0)
print(lista)

arq2 = open('feminino.txt','w')
arq2.write('Alunas do sexo Feminino:\n')
arq3 = open('masculino.txt','w')
arq3.write('Alunos do sexo masculino:\n')

for i in lista:
     if i[1] == 'F':
          arq2.write(i[0] + '\n')
     if i[1] == 'M':
          arq3.write(i[0] + '\n')
arq2.close()
arq3.close()

