from corredores import*
lista = le_corredores_e_tempo()

print(melhor(lista))

print(mais_lento(lista))



















































'''
menor = 100

for i in lista_corredores:
     if min(i[1:]) < menor:
          menor = min(i[1:])
          nome = i[0]
print('A melhor volta foi do ', nome, 'em ', menor, 'segundos.')


string = str(menor)
converter_string = []
for i in lista_corredores:
     linha = []
     for x in range(len(i)):
          linha.append(str(i[x]))
     converter_string.append(linha)
indice = []
for i in converter_string:
     for x in range(len(i)):
          if i[x] == string:
               indice.append(i[0])
               indice.append(x)
print('o Corredor', indice[0], 'fez o melhor tempo na volta ', indice[1])

'''
