import Fifo
l1=Fifo.Fifo()

quantLista=int(input('Digite a quantidade de elementos da lista:'))

for i in range(quantLista):
    elemento=input('Insira o '+str(i+1)+'º elemento:')
    l1.inserir(elemento)
print('\n')
l1.show()
print('\n')

for i in range(quantLista+1):
    if l1.estahVazia()==True:
        print("\nA lista está vazia!")
    else:
        print("----- Removendo",l1.pegaPrim().info,"-----")
        l1.remover()
        l1.show()
    
