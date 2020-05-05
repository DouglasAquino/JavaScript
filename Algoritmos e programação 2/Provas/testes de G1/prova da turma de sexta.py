# G1 
'''
lista = [["A", "B", "C", "D", "E"], ["X", "A"], ["X", "K", "Z"], ["L"]]
listamanho = len(lista)
print(lista)
for i in range(listamanho):

     if len(lista[i]) != listamanho:
          listinha = len(lista[i])

          while listamanho > listinha:
               ultimovalor = lista[i][len(lista[i])-1]
               lista[i].append(ultimovalor)

               listinha = len(lista[i])

          while listamanho < listinha:
               lista[i].pop()

               listinha = len(lista[i])
print(lista)
'''
'''
lista = [["A", "B", "C", "D", "E"], ["X", "A"], ["X", "K", "Z"], ["L"]]
listamanho = len(lista)
print(lista)
for i in range(listamanho):

     if len(lista[i]) != listamanho:

          while listamanho > len(lista[i]):
               lista[i].append(lista[i][len(lista[i])-1])


          while listamanho < len(lista[i]):
               lista[i].pop()

print(lista)
'''

# Verifica os elementos da primeira lista e deixa todos do tamanho dela


lista = [["A", "B", "C", "D", "E"], ["X", "A"], ["X", "K", "Z"], ["L", "M", "J", "A", "Q", "f"]]
print(lista)
for i in range(len(lista)):

     if len(lista[i]) != len(lista[0]):

          while len(lista[0]) > len(lista[i]):
               lista[i].append(lista[i][len(lista[i])-1])


          while len(lista[0]) < len(lista[i]):
               lista[i].pop()

print(lista)






# Insere o primeiro elemento

'''
lista = [["A", "B", "C", "D", "E"], ["X", "A"], ["X", "K", "Z"], ["L", "A"]]
listamanho = len(lista)
print(lista)
for i in range(listamanho):

     if len(lista[i]) != listamanho:

          while listamanho > len(lista[i]):
               lista[i].append(lista[i][0])


          while listamanho < len(lista[i]):
               lista[i].pop()

print(lista)
'''
'''
lista = [["Jorge", 6.7, 8, 75],
         ["Luan", 6, 6, 40],
         ["Maria", 4, 5, 90]]

for i in range(len(lista)):
     if lista[i][1] >= 6 and lista[i][2] >= 6 and lista[i][3] >= 75:
          lista[i].append("Aprovado")
     elif lista[i][1] < 6 or lista[i][2] < 6 and lista[i][3] > 75:
          lista[i].append("Em recuperação")
     elif lista[i][1] < 6 and lista[i][2] < 6 or lista[i][3] < 75:
          lista[i].append("Reprovado")
print(lista)
'''
# adiciona a media ao final e diz a aprovacao
'''
lista = [["Jorge", 6.7, 8],
         ["Luan", 6, 6],
         ["Maria", 4, 5]]

for i in range(len(lista)):
     lista[i].append(((lista[i][1] + (lista[i][2]*2))/3))
print(lista)

for i in range(len(lista)):
     if lista[i][3] >= 6:
          lista[i].append("Aprovado")
     else:
          lista[i].append("Reprovado")
print(lista)
'''






















































