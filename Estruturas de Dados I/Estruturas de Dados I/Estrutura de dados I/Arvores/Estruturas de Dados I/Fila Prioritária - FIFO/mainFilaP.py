import FilaP
f1=FilaP.FilaP()

op=int(input('1 - Inserir\n2 - Remover\n3 - Ver Filas\n0 - Encerrar\nEscolha uma opção para continuar:'))

while op!=0:
    if op==1:
        elem=input('Digite um elemento:')
        prio=int(input('Digite a prioridade do elemento:'))
        while prio!=1 and prio!=2 and prio!=3 and prio!=4:
            print('Prioridade inválida!')
            prio=int(input('Digite a prioridade do elemento:'))
        f1.inserir(elem,prio)
    elif op==2:
        if f1.estahVazia()==True:
            print('\nFilas vazias!')
        else:
            f1.remover()
            print('\nElemento removido!')        
    elif op==3:
        ver=int(input('\n1 - Fila 1\n2 - Fila 2\n3 - Fila 3\n4 - Fila 4\n5 - Todas\n0 - Sair\nEscolha uma opção para continuar:'))
        while ver!=0:
            if ver==1:
                f1.show1()
            elif ver==2:
                f1.show2()
            elif ver==3:
                f1.show3()
            elif ver==4:
                f1.show4()
            elif ver==5:
                print('\nFila 1:')
                f1.show1()
                print('\nFila 2:')
                f1.show2()
                print('\nFila 3:')
                f1.show3()
                print('\nFila 4:')
                f1.show4()
            else:
                print('Opção inválida!')
            ver=int(input('\n1 - Fila 1\n2 - Fila 2\n3 - Fila 3\n4 - Fila 4\n5 - Todas\n0 - Sair\nEscolha uma opção para continuar:'))     
    else:
        print('Opção inválida!')
    op=int(input('\n1 - Inserir\n2 - Remover\n3 - Ver Filas\n0 - Encerrar\nEscolha uma opção para continuar:'))
