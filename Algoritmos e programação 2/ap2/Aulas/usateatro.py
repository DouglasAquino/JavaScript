from teatro import *
arq = open('teatro.txt','r')
conteudo = arq.read()
arq.close()

print(vagasTotais(conteudo))
print(vagasPorFila(conteudo,2))
print(faturamento(conteudo))
verMapa(conteudo)
comprarIngresso(conteudo)
casal(conteudo,13)
