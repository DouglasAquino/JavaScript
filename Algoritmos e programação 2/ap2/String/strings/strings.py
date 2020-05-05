word = "palavra"
letra = word[3]
print(letra)

print('-------------------------------------------------')

word = "palavra"
comprimento = len(word)
ultima = word[comprimento - 1]
print(ultima)

print('-------------------------------------------------')

word = "palavra"
i = 0
while i < len(word):
     print(word[i])
     i += 1
print()

for letra in word:
     print(letra)
     
print('-------------------------------------------------')

prefixos = "BCDFGJLMNPRT"
sufixo = "ato"
for letra in prefixos:
     print(letra + sufixo)

print('-------------------------------------------------')

nomes = "Pedro, Paulo e Maria"
print(nomes[0:5])
print(nomes[7:12])
print(nomes[15:21])

print('-------------------------------------------------')

palavra = "ovo"
if palavra < "ovo":
    print ("Sua palavra, " + palavra + ", vem antes de ovo.")
elif palavra > "ovo":
    print ("Sua palavra, " + palavra + ", vem depois de ovo.")
else:
    print ("Sua palavra é ovo")
    
print('-------------------------------------------------')

palavra = "Paumas"
print(palavra)
palavra = palavra.replace('u', 'l')
print(palavra)

print('-------------------------------------------------')

palavra = "Paunas"
print(palavra)
palavra = palavra.replace('un', 'lm')
print(palavra)

print('-------------------------------------------------')


palavra = "orangotango"
indice = palavra.find("o")
print("Letra o na posicção: ", indice)
print("Letra t na posição: ", palavra.find("t"))

print('-------------------------------------------------')

palavra = "orangotango"
indice = palavra.find("an")
print("Caracteres \"an\" na posição: ", indice)

print('-------------------------------------------------')

palavra = "orangotango"
indice = palavra.find("an", 3)
print("Caracteres \"an\" na posição: ", indice)

print('-------------------------------------------------')

palavra = "orangotango"
indice = palavra.find("an", 3, 7)
print("Caracteres \"an\" na posição: ", indice)

print('-------------------------------------------------')

palavra = "orangotango"
quant = palavra.count("o")
print("Quantidade de \"o\":", quant)
print("Quantidade de \"an\":", palavra.count("an"))

print('-------------------------------------------------')

# palavras maiusculas
palavra = "orangotango"
print(palavra.upper())
print(palavra)

print('-------------------------------------------------')

# maiusculas e minusculas
frase = "um Pequeno passo"
# primeira letra maiuscula
print(frase.capitalize())
# Primeira letra de cada palavra em letra maiscula
print(frase.title())
# inverte as letra
print(frase.swapcase())
# primeiras maiusculas depois inverte
print(frase.title().swapcase())

print('-------------------------------------------------')

frase = "chico branco"
if frase.islower():
    print("A frase está toda em minúsculas")
elif frase.isupper():
    print("A frase está toda em maiúsculas")
elif frase.istitle():
    print("A frase tem somente as primeiras letras em maiúsculas ")

print('-------------------------------------------------')

texto = "jumentino1"
if texto.isalnum():
    print("O texto contém somente letras ou números")
else:
    print("O texto contém outros símbolos")

print('-------------------------------------------------')

texto = "aaaaaaaaaaa11111111aaaaaaaaaaa"
if texto.isalpha():
    print("O texto contém somente letras")
elif texto.isdigit():
    print("O texto contém somente números")
elif texto.isalnum():
    print("O texto contém somente letras ou números")

print('-------------------------------------------------')

texto = "abc"
if texto.startswith("a"):
    print("Começa com a")

if texto.endswith("c"):
    print("Termina com c")
palavra = "bc"
if palavra in texto:
    print(palavra, "está em", texto)
print('-------------------------------------------')

texto = "A bc def"
lista = texto.split(" ")
print (lista)

print('-------------------------------------------')

texto = '111.222.333-44'
lista1 = texto.split('-')
print(lista1)
lista2 = lista1[0].split('.')
print(lista2)

print('-------------------------------------------')

lista=['A','B','C']
juncao = ' depois de '
novaString = juncao.join(lista)
print("Lista =", lista)
print("Texto =", novaString)
































































































































     
