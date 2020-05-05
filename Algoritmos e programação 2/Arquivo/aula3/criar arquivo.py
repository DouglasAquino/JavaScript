#dessa forma caso o arquivo ñ exita ele será criado

arq = open('tem.txt','w')

# \n para pular linha
arq.write('Teste1\n')
arq.write('Teste2\n')
arq.write('Teste')

# so adiciona se no codigo tiver o close.
arq.close()


texto = 'um teste testando o teste'
lista = texto.split('te')
for i in lista:
     print(i)
juntar = 'te'.join(lista)
print(juntar)
