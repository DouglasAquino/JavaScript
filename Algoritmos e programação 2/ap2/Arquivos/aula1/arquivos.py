def le_arquivo(arquivo):
     arq = open(arquivo,'r')
     conteudo = arq.read()
     arq.close()
     return print(conteudo)

def le_arquivo_lista(arquivo):
     arq = open(arquivo,'r')
     conteudo = arq.read()
     arq.close()
     lista = conteudo.split('\n')
     return print(lista)
'''
def muda_cabecalho(arquivo):
     arq = open(arquivo, 'w')
     conteudo = arq.read()
     lista = []
     for i in conteudo:
          l = i.split(',')
          l[0] = 'Academicas:'
          lista.append(l)
     for i in lista:
          arq.write(i)
     arq.close()'''
                  
     

def acrescenta_linha(arquivo):
     arq = open(arquivo,'a')
     n = input('Digite o nome: ')
     arq.write('\n')
     arq.write(n + ',')
     arq.close()



def inverte_arquivo(arquivo):
    arq=open(arquivo, 'r')
    conteudo=arq.read()
    lista=conteudo.split('\n')
    inversao=lista[::-1]
    ordem=sorted(inversao)
    arqInver=open('inversão.txt','w')
    for  i,n in enumerate(inversao):
        arqInver.write(n)
        arqInver.write('\n')
    arqInver.close()
