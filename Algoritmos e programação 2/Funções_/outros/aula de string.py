# Array vetor ou arranjo
'''
word = "palavra"
letra = word[3]
print(letra)
print()

i = 0
while i < len(word):
    print(word[i])
    i += 1
print()

for letra in word:
    print(letra)
print()

# soma a letra com o sufixo ato concatenação 
prefixos = "BCDFGJLMNPRT"
sufixo = "ato"
for letra in prefixos:
    print (letra + sufixo)
print()

palavra = input("Digite uma palavra:")
if palavra < "ovo":
    print ("Sua palavra, " + palavra + ", vem antes de ovo.")
elif palavra > "ovo":
    print ("Sua palavra, " + palavra + ", vem depois de ovo.")
else:
    print ("Sua palavra é ovo")

palavra = 'aeiouou'
palavra = palavra.replace('u', '\n')
print(palavra)
'''

p1 = 'abc'
p2 = 'def'

print(p1, p2)
print(p1 + p2)
print('aeiaei'.replace('ae', 'xy'))
