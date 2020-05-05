import PilhaD
p1=PilhaD.PilhaD()

nome='gon'
resultado=False
i=0
while i<len(nome):
    p1.push(nome[i].lower())
    i+=1
i=0
while i<len(nome):
    if p1.getTopo()==nome[i].lower():
        p1.pop()
        resultado=True
    else:
        resultado=False
        i=len(nome)
    i+=1

if p1.estahVazia() and resultado==True:
    print('É Polindromo!')
else:
    print('Não é Polindromo!')




