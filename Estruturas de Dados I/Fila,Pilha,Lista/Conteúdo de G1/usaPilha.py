import PilhaD
p1= PilhaD.PilhaD()
p2= PilhaD.PilhaD()

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

p3= PilhaD.PilhaD()
while p1.estahVazia != True or p2.estahVazia != True:
    if p1() > p2():
        p3.push(p1)
        p1.pop()
    else:
        p3.push(p2)
        p2.pop()
p3.show
    
