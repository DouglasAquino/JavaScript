import PilhaD
p1=PilhaD.PilhaD()

nome='ESTE EXERCICIO E MUITO FACIL'
resultado=False
lista = nome.split(" ")
inverso=''

for i in range(len(lista)):
    for z in range(len(lista[i])):
        p1.push(lista[i][z])
    for z in range(len(lista[i])):
        #print(""inverso)
        print(p1.getTopo())
        inverso+=p1.getTopo()
        p1.pop()
    inverso+=' '
    

p1.show()
print(nome)
print(inverso)





