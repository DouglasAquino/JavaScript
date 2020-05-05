import PilhaD

p2 = PilhaD.PilhaD()
p2.push('B')
p2.push('C')
p2.push('F')
p2.push('G')
p2.push('I')
p2.push('J')
p2.push('K')


print("TOPO antes")
print(p2.getTopo())

print("Funcao topop:")
print(p2.topop())

print("Novo topo da Pilha")
print(p2.getTopo())
