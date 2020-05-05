#Palindromo
import Pilha
p=Pilha.Pilha()
expressao = 'arara'
i=0
j=0
while j<len(expressao):
    p.push(expressao[j])
    j+=1
while i<len(expressao) and expressao[i]==p.getTopo():
        p.pop()
    i+=1
if p.estahVazia():
    print("A palavra: ",expressao+" é um palíndromo")
else:
    print("A palavra:",expressao+" é um palíndromo")
