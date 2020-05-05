import Baralho

l1=Baralho.BaralhoA()
l2=Baralho.BaralhoB()
nA=0
nB=0

def empilharCartas():
    global nA
    global nB
    qtdCartas=int(input('Qual a quantidade de cartas para cada jogador:'))
    if qtdCartas>=1 and qtdCartas<=20:
        print('Digite as', qtdCartas,'cartas para o Jogador A!')
        nA=nA+qtdCartas
        nB=nB+qtdCartas
        for i in range(qtdCartas):
            a=int(input('Insira a '+str(i+1)+'º carta:'))
            l1.inserirTopo(a)
        print('Faça o mesmo agora com o Jogador B!')
        for i in range(qtdCartas):
            b=int(input('Insira a '+str(i+1)+'º carta:'))
            l2.inserirTopo(str(b))   
    else:
        print('O número de cartas deve ser >=1 e <=20!\nDigite novamente!!!')
        empilharCartas()
    
def combate():
    global nA
    global nB
    while nA!=0 and nB!=0:
        p1=int(l1.getPrim())
        p2=int(l2.getPrim())
        if p1>p2:
            if (p1-1)==0:
                l1.removerTopo()
                nA-=1
            else:
                l1.inserirBase(p1-1)
                l1.removerTopo()
                
            if (p2-1)==0:
                l2.removerTopo()
                nB-=1
            else:
                l1.inserirBase(p2-1)
                l2.removerTopo()
                nA+=1
                nB-=1
        else:
            if p2>p1:
                if (p2-1)==0:
                    l2.removerTopo()
                    nB-=1
                else:
                    l2.inserirBase(p2-1)
                    l2.removerTopo()
                

                if (p1-1)==0:
                    l1.removerTopo()
                    nA-=1
                else:
                    l2.inserirBase(p1-1)
                    l1.removerTopo()
                    nB+=1
                    nA-=1
            else:
                if (p1-1)==0:
                    l1.removerTopo()
                    nA-=1
                else:
                    l1.inserirBase(p1-1)
                    l1.removerTopo()

                if (p2-1)==0:
                    l2.removerTopo()
                    nB-=1
                else:
                    l2.inserirBase(p2-1)
                    l2.removerTopo()
                    
        
    if nA==0 and nB==0:
        print("E")
    elif nB==0:
        print("A")
    elif nA==0:
        print("B")
    
    
    




    
empilharCartas()   
combate()

