arq=open('cidades.csv','r')
lista=arq.read().split('\n')
arq.close()


def cidade(lista):
    l=[]
    for i in lista:
        lista1=i.split(';')
        l.append(lista1)
        lista=l
    return lista

def ver(lista):
    a=lista.pop()
    for i in lista:
        print(i)

def distancia(lista,a,b):
    
    linha=0
    coluna=0
    
    for i in range(len(lista)):
        if lista[i][0]==a:
            linha=i
    
    for i in range(len(lista)):
        if lista[0][i]==b:
            coluna=i

    posicao=lista[linha][coluna]
    return posicao

def maiorDistancia(lista,a):
    m=[]
    dic={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}
    for i in lista:
        m.append(i[dic[a]])
    m.pop(0)
    maior=max(m)

    return maior

def cidadeMaisLonge(lista,a):
    
    m=[]
    longe=[]
    dic={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}
    for i in lista:
        m.append(i[dic[a]])

    m.pop(0)
    maior=max(m)
    for i in range(len(m)):
        if m[i]==maior:
            p=i
            longe.append(lista[p+1][0])

    junta='\n'.join(longe)
    return junta   

    
    
                
