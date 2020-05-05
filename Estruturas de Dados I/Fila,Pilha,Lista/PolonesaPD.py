import PilhaD

l=PilhaD.PilhaD()

p='53+*2'

op1=0
op2=0

for i in p:
    if i.isdigit():
        l.push(int(i))
    
        
    else:
        op2=l.getTopo()
        l.pop()
        op1=l.getTopo()
        l.pop()

        if i == '+':
            l.push(op1+op2)

        elif i == '-':
            l.push(op1-op2)

        elif i == '*':
            l.push(op1*op2)

        else:
            l.push(op1/op2)

print(l.getTopo())
        
        
        
