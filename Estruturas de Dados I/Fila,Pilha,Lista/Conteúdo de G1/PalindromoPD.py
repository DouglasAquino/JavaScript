import PilhaD
l=PilhaD.PilhaD()

p=input('Digite um nome:')

for i in p:
    l.push(i)

for i in p:
    if i == l.getTopo():
        l.pop()
if l.estahVazia():
    print('É um palindromo!')

else:
    print('Não é um palindromo!')
