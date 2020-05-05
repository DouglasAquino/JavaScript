# Exemplo 1
word = "palavra"
letra = word[3]
print (letra)
print()

# Exemplo 2
word = "palavra"
comprimento = len(word)
ultima = word[comprimento-1]
print(ultima)
print()

# Exemplo 3
word = "palavra"
i = 0
while i<len(word):
    print(word[i])
    i+=1
print()

# Exemplo 4
word = "palavra"
for letra in word:
    print (letra)
print()

# Exemplo 5
prefixos = "BCDFGJLMNPRT"
sufixo = "ato"
for letra in prefixos:
    print (letra + sufixo)
print()

# Exemplo 6
nomes = "Pedro, Paulo e Maria"
print (nomes[0:5])
print (nomes[7:12])
print (nomes[15:21])
print()

# Exemplo 7
palavra = input("Digite uma palavra:")
if palavra < "ovo":
    print ("Sua palavra, " + palavra + ", vem antes de ovo.")
elif palavra > "ovo":
    print ("Sua palavra, " + palavra + ", vem depois de ovo.")
else:
    print ("Sua palavra é ovo")
print()

# Exemplo 8
palavra = "Paumas"
print(palavra)
palavra = palavra.replace("u","l")
print(palavra)
print()

# Exemplo 9
palavra = "Paunas "
print(palavra)
palavra = palavra.replace("un","lm")
print(palavra)
print()

# Exemplo 10
palavra = "orangotango"
indice = palavra.find("o")
print("Letra o na posição:", indice)
print("Letra t na posição:", palavra.find("t"))
print()

# Exemplo 11
palavra = "orangotango"
indice = palavra.find("an")
print("Caracteres \"an\"  na posição:", indice)
print()

# Exemplo 12
palavra = "orangotango"
indice = palavra.find("an",3)
print("Caracteres \"an\"  na posição:", indice)
print()

# Exemplo 13
palavra = "orangotango"
indice = palavra.find("an",3,7)
print("Caracteres \"an\"  na posição:", indice)
print()

# Exemplo 14
palavra = "orangotango"
quant = palavra.count("o")
print("Quantidade de \"o\":", quant)
print("Quantidade de \"an\":", palavra.count("an"))
print()

# Exemplo 15
palavra = "orangotango"
print(palavra.upper())
print(palavra)
print()

# Exemplo 16
frase = "um Pequeno passo"
print(frase.capitalize())
print(frase.title())
print(frase.swapcase())
print(frase.title().swapcase())
print()

# Exemplo 17
frase = input("Digite uma palavra: ")
if frase.islower():
    print("A frase está toda em minúsculas")
elif frase.isupper():
    print("A frase está toda em maiúsculas")
elif frase.istitle():
    print("A frase tem somente as primeiras letras em maiúsculas ")
print()

# Exemplo 18
texto = input("Digite um texto: ")
if texto.isalnum():
    print("O texto contém somente letras ou números")
else:
    print("O texto contém outros símbolos")
print()

# Exemplo 19
texto = input("Digite um texto: ")
if texto.isalpha():
    print("O texto contém somente letras")
elif texto.isdigit():
    print("O texto contém somente números")
elif texto.isalnum():
    print("O texto contém somente letras ou números")
print()

# Exemplo 20
texto = "abc"
if texto.startswith("a"):
    print("Começa com a")
if texto.endswith("c"):
    print("Termina com c")
palavra = "bc"
if palavra in texto:
    print(palavra, "está em", texto)
print()

# Exemplo 21
texto = "A bc def"
lista = texto.split(" ")
print (lista)
print()

# Exemplo 22
texto = '111.222.333-44'
lista1 = texto.split('-')
print(lista1)
lista2 = lista1[0].split('.')
print(lista2)
print()

# Exemplo 23
lista=['A','B','C']
juncao = ' depois de '
novaString = juncao.join(lista)
print("Lista =", lista)
print("Texto =", novaString)
























































