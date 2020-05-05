arq = open('notas.txt','r')
conteudo = arq.read().replace(' ', ',').split('\n')
arq.close()
lista = []
for i in conteudo:
     lista.append(i.split(','))

for i in lista:
     if float(i[1]) >= 6 and float(i[2]) >= 6 and int(i[3]) >= 75:
          i.append('Aprovado')
     elif float(i[1]) >= 6 and float(i[2]) < 6 and int(i[3]) >= 75:
          i.append('Recuperação')
     else:
          i.append('Reprovado')

print(lista)

arq2 = open('notas.txt','w')
for i in lista:
     arq2.write(i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + i[3] + ' ' + i[4] + '\n')
arq2.close()
     
