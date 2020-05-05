import PilhaD
p1=PilhaD.PilhaD()

expressao='([)(())'
i=0
while i<len(expressao):
    if expressao[i]=='(' or expressao[i]=='[':
        p1.push(expressao[i])
    elif expressao[i]==')':
        if not p1.estahVazia() and p1.getTopo().info=='(':
            p1.pop()
        else:
            print('Sobrando )')
            i=len(expressao)
        
    elif expressao[i]==']':
        if not p1.estahVazia() and p1.getTopo().info=='[':
            p1.pop()
        else:
            print('Sobrando ]')
            i=len(expressao)
    i+=1

if p1.estahVazia():
    print('Tudo ok!')
else:
    print('Erro')
