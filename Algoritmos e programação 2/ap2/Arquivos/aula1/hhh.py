def le_arquivo():
     arq = open('arquivo.txt','r')
     conteudo = arq.read()
     arq.close()
     print(conteudo)

     lista = conteudo.split('\n')
     print(lista)
