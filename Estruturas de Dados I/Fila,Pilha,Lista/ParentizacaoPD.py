import PilhaD
l=PilhaD.PilhaD()

p=input('Digite uma equação:')

erro=False

for i in p:
    if i == '(':
        l.push(i)

    elif i == ')':
        if l.estahVazia():
            erro=True
        else:
            l.pop()

if erro or l.estahVazia() == False:
    print('Parentização incorreta!')

elif erro == False and l.estahVazia():
    print('Parentrização correta!')

