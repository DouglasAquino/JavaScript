def leDados(arquivo):
    arq = open(arquivo,'r')
    conteudo = arq.read()
    arq.close()
    return conteudo

def montaDicPrecos(conteudo):
    conteudo=conteudo.replace(',','.')
    lista = conteudo.split('\n')
    dic = {}
    for i in lista[1:]:
        listaTemp = i.split(';')
        dic[listaTemp[0]]=float(listaTemp[1])
    return dic

def montaDicVendas(conteudo):
    lista = conteudo.split('\n')
    contaVendas = {}
    for i in lista[1:]:
        listaTemp = i.split(',')
        contaVendas[listaTemp[0]] = contaVendas.get(listaTemp[0],0) + int(listaTemp[1])
    return contaVendas

def montaDicTotal(dicPrecos,dicVendas):
    dic = {}
    for i in dicVendas:
        dic[i]=dicVendas[i]*dicPrecos[i]
    return dic

def calculaTotal(dicTotal):
    total = 0
    for i in dicTotal:
        total += dicTotal[i]
    return total

def escreveArquivo(dicVendas,dicPrecos,dicTotal):
    arq = open('total.txt','w')
    arq.write('Produto;Quant;Valor Unid;Valor Total')
    for i in sorted(dicTotal):
        arq.write(i+';'+str(dicVendas[i])+';'+str(dicPrecos[i])+';'+str(dicTotal[i])+'\n')
    arq.write('Total'+';'+str(calculaTotal(dicTotal)))


    
      


