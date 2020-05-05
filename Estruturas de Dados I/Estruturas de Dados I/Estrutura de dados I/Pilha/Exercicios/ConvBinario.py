import PilhaD
p=PilhaD.PilhaD()
num=int(input("Numero:"))
base=int(input("Base:"))
while num >=base:
    p.push(str(num%base))
    num=num//base
p.push(num)

while not p.estahVazia():
    print(p.getTopo(), end=(''))
    p.pop()
    
