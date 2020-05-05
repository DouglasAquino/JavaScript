import PilhaD
p1=PilhaD.PilhaD()

num=int(input("Digite um número:"))
binario=''
while num != 0:
    p1.push(str(num % 2))
    num = int(num / 2)

while p1.getTopo()!=None:
    binario+=p1.getTopo()
    p1.pop()

print(binario)
