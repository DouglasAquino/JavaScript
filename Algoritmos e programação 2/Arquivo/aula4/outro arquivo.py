# outro arquivo

arq = open('tem.txt','r')
conteudo = arq.read()

# o read ñ da pal sem o close, mas coloque
arq.close()
print(conteudo)

# read retorna uma string
# readlines retorna uma lista com strings
arq = open('tem.txt','r')
conteudo2 = arq.readlines()
arq.close()
print(conteudo2)


# Eliminar \n

lista = conteudo.split('\n')
print(lista)


arq = open('tem.txt','r')
lista = arq.read().split('\n')
arq.close()
print(lista) #['Teste1', 'Teste2', 'Teste3']

# contar quantos 3 tem no arquivo

# endswith para verificar ultimas palavras
# startswith para inicio

cont = 0
for i in lista:
     if i[-1] == '3':
          cont += 1
print(cont)
