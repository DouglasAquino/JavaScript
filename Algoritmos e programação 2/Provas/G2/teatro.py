def quantOcupados(conteudo):
    return conteudo.count('O')



def filasMaisOcupadas(conteudo):
    listaDeFilas = conteudo.split('\n')[1:]
    fat = 0
    lista = []
    for i in listaDeFilas:
        lista.append([i[:2], i.count('O')])
    maxi = 0
    for i in lista:
        if i[1] > maxi:
            maxi = i[1]
    nova = []
    for i in lista:
        if i[1] == maxi:
            nova.append(i[0])
    for i in nova:
        print(int(i))

