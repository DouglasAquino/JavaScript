from teatro import *
arq = open('teatro.txt','r')
conteudo = arq.read()
arq.close()
print('Quantidade de lugares ocupados', quantOcupados(conteudo))

print('Filas com mais poltronas ocupadas:')
filasMaisOcupadas(conteudo)

'''
print('Filas onde cabem 4 pessoas lado a lado: ')
ondeCabemPessoasLadoALado(conteudo,4)

print('Filas onde cabem 8 pessoas lado a lado: ')
ondeCabemPessoasLadoALado(conteudo,8)
print('Filas onde cabem 11 pessoas lado a lado: ')
ondeCabemPessoasLadoALado(conteudo,11)
'''
