arq = open('notas.txt','r')
lista = arq.read().replace(',', '.').split('\n')
arq.close()
print(lista)

lista_notas = []
for i in lista:
     lista_notas.append(i.split(';'))
print(lista_notas)

for i in lista_notas:
     if float(i[1]) >= 6 and float(i[2]) >= 6 and float(i[3]) >= 75:
          i.append('Aprovado')
     elif float(i[1]) < 6 and float(i[2]) < 6 or float(i[1]) > 5 and float(i[2]) > 5 and float(i[3]) > 75:
          i.append('Recuperação')
     else:
          i.append('Reprovado')

print(lista_notas)



arq2 = open('notas.txt','w')
for i in lista_notas:
     arq2.write(i[0] + ';' + i[1] + ';' + i[2] + ';' + i[3] + ';' + i[4] + '\n')
arq2.close()


