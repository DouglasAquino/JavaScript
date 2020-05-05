import PilhaD
p1=PilhaD.PilhaD()

nome='ISSO ESTA LEGAL'
resultado=False
lista = nome.split(" ")
inverso=''

for i in range(len(lista)):
    for z in range(len(lista[i])):
        p1.push(lista[i][z])
    for z in range(len(lista[i])):
        inverso+=p1.getTopo().info
        p1.pop()
    inverso+=' '

p1.show()
print(nome)
print(inverso)





