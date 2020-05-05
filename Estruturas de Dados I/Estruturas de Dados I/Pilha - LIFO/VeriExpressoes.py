import PilhaD
p1=PilhaD.PilhaD()

expressao='[]'
resultado=False
i=0


while i<len(expressao):
    if expressao[i]=='(' or expressao[i]=='[' or expressao[i]=='{':
        p1.push(expressao[i])
    elif expressao[i]==')' or expressao[i]==']' or expressao[i]=='}':
        if not p1.estahVazia():
            if p1.getTopo()=='(' and expressao[i]==')':
                p1.pop()
            elif p1.getTopo()=='[' and expressao[i]==']':
                p1.pop()
            elif p1.getTopo()=='{' and expressao[i]=='}':
                p1.pop()
            resultado=True
        else:
            print("Sobrando",expressao[i])
            resultado=False
            i=len(expressao)
    i+=1
           
        
if p1.estahVazia() and resultado==True:
    print('Tudo ok!')
elif not p1.estahVazia():
    print('ERRO!')


