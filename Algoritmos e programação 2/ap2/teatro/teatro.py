def vagasTotais(conteudo):
    return conteudo.count('L')

def vagasPorFila(conteudo,fila):
    listaDeFilas = conteudo.split('\n')[1:]  # prestem atenção que esse slice removeu a primeira linha da lista
    return listaDeFilas[fila].count('L')
    
def faturamento(conteudo):
    fat = 0
    listaDeFilas = conteudo.split('\n')[1:]
    for i in listaDeFilas[0:4]:
        fat+=i.count('O')*50
    for i in listaDeFilas[4:10]:
        fat+=i.count('O')*40
    for i in listaDeFilas[10:]:
        fat+=i.count('O')*30
    return fat
    
def verMapa(conteudo):
    print(conteudo)

def comprarIngresso(conteudo):
    dic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
    
    fila = int(input('Qual a fila desejada? '))
    poltrona = input('Qual a poltrona desejada? ')

    conteudo = conteudo.replace('  ',' ')   # este é para os arquivos que têm
                                            # dois espaços entre o número da fila e
                                            # a primeira poltrona

    listaDeFilas = conteudo.split('\n')[1:] # prestem atenção que esse slice removeu a primeira linha da lista
    listaDePoltronas=listaDeFilas[fila].split(' ')[1:] # prestem atenção que esse slice removeu a primeira coluna (aquela dos números de cada fila)

    if listaDePoltronas[dic[poltrona]]=='O':
        print('Sinto muito. Poltrona já ocupada')
    else:
        listaDePoltronas[dic[poltrona]]='O'
        listaDeFilas[fila]=str(fila)+' '+' '.join(listaDePoltronas)
        arq = open ('novoteatro.txt','w')  # é para salvar no mesmo arquivo. Deixei com outro nome paar vc observar a mudança
        arq.write('X  A B C D E F G H I J\n')
        for i in listaDeFilas:
            arq.write(i+'\n')
        arq.close()

def casal(conteudo,fila):
    dic = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J'}
    conteudo = conteudo.replace('  ',' ')
    listaDeFilas = conteudo.split('\n')[1:] # prestem atenção que esse slice removeu a primeira linha da lista
    listaDePoltronas=listaDeFilas[fila].split(' ')[1:] # prestem atenção que esse slice removeu a primeira coluna (aquela dos números de cada fila)
    i = 1
    print(listaDePoltronas)
    while i<9:
        #print(i)
        if listaDePoltronas[i]=='L' and listaDePoltronas[i-1]=='L' and listaDePoltronas[i+1]=='L':
            # este if é considerando o erro na questão que em vez de pedir duas posições livres acabou pedindo três
            print('Poltrona ',dic[i],' livre')
        i+=1
            
        
    
        
        

    
    

    
