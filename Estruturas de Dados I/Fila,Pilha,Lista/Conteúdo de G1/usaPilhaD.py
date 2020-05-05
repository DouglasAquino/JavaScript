import PilhaD
p1 = PilhaD.PilhaD()
p2 = PilhaD.PilhaD()
p1.push('A')
p1.push('D')
p1.push('E')
p1.push('H')
p2.push('B')
p2.push('C')
p2.push('F')
p2.push('G')
p2.push('I')
p2.push('J')
p2.push('K')

p3 = PilhaD.PilhaD()

while not p1.estahVazia() and not p2.estahVazia():
    if p1.getTopo() > p2.getTopo():
        p3.push(p1.getTopo())
        p1.pop()
    else:
        p3.push(p2.getTopo())
        p2.pop()

if not p1.estahVazia():
    while not p1.estahVazia():
        p3.push(p1.getTopo())
        p1.pop()
else:
    while not p2.estahVazia():
        p3.push(p2.getTopo())
        p2.pop()


while not p3.estahVazia():
    print(p3.getTopo())
    p3.pop()
