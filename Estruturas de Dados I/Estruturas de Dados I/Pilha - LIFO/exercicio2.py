import PilhaD
p=PilhaD.PilhaD()
p2=PilhaD.PilhaD()
p3=PilhaD.PilhaD()



palavra= "ABCBA"

for i in palavra: 
    p.push(i)
    
p.show()
print("------")

cont=0
while cont<len(palavra):
    if palavra[cont]==p.getTopo() and palavra[cont]!="C":
        p2.push(p.getTopo())
        p.pop()
    cont+=1
        
p.show()
print("-----")
p2.show()

p.pop()


print("-----")
p3.show()

print("-----")



for i in range(cont):
    if p.getTopo() == p2.getTopo():
        print("A string é do formato xCy")
        p.pop()
        p2.pop()
    
    else:
        print("A string nn e do formato")
