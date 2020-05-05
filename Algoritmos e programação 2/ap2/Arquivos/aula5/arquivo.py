arq = open('arquivo.txt','r')
conteudo = arq.read()
arq.close()

print(conteudo)

listadelinhas = conteudo.split('\n')
print(listadelinhas)

arq = open('arquivo.txt','w')

for i in listadelinhas:
     print(i)
     lista = i.split(',')
     if lista[0] == 'Triangulo':
          base = float(lista[1])
          altura = float(lista[2])
          area = round((base * altura)/2, 1)
          arq.write(i + ',' + str(area) + '\n')

     elif lista[0] == 'Retangulo':
          l1 = float(lista[1])
          l2 = float(lista[2])
          area = round(l1 * l2, 1)
          arq.write(i + ',' + str(area) + '\n')

     elif lista[0] == 'Circulo':
          raio = float(lista[1])
          area = round(3.14 * raio **2, 1)
          arq.write(i + ',' + str(area) + '\n')

     elif lista[0] == 'Quadrado':
          lado = float(lista[1])
          area = (lado**2)
          arq.write(i + ',' + str(area) + '\n')

arq.close()
