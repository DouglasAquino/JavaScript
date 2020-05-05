print('REPLACE: MUDA UMA OU MAIS LETRAS!')
palavra = "Paumas"
print(palavra)
palavra = palavra.replace("u","l")
print(palavra)
palavra = "Paunas "
print(palavra)
palavra = palavra.replace("un","lm")
print(palavra)
print('\n')

print('FIND')

palavra = "orangotango"
print(palavra)
indice = palavra.find("o")
print("Letra o na posição:", indice)
print("Letra t na posição:", palavra.find("t"))
indice = palavra.find("an")
print("Caracteres \"an\"  na posição:", indice)
indice = palavra.find("an",3)
print("Caracteres \"an\"  na posição:", indice)
indice = palavra.find("an",3,7)
print("Caracteres \"an\"  na posição:", indice)
print('\n')

print('COUNT')
palavra = "orangotango"
print(palavra)
quant = palavra.count("o")
print("Quantidade de \"o\":", quant)
print("Quantidade de \"an\":", palavra.count("an"))
print('\n')

print('MAIÚSCULAS')
palavra = "orangotango"
print(palavra.upper())
print(palavra)
print('\n')

frase = "um Pequeno passo"
print(frase.capitalize(),'CAPITALIZE')
print(frase.title(),'TITLE')
print(frase.swapcase(),'SWAPCASE') 
print(frase.title().swapcase(),'SWAPCASE + TITLE')
print('\n')
'''
#Algumas verificações
frase = input("Digite uma palavra: ")

if frase.islower():
    print("A frase está toda em minúsculas")
elif frase.isupper():
    print("A frase está toda em maiúsculas")
elif frase.istitle():
    print("A frase tem somente as primeiras letras em maiúsculas ")


texto = input("Digite um texto: ")

if texto.isalnum():
    print("O texto contém somente letras ou números")
else:
    print("O texto contém outros símbolos")
texto = input("Digite um texto: ")

if texto.isalpha():
    print("O texto contém somente letras")
elif texto.isdigit():
    print("O texto contém somente números")
elif texto.isalnum():
    print("O texto contém somente letras ou números")


'''
texto = "abc"
print(texto)

if texto.startswith("a"):
    print("Começa com a")

if texto.endswith("c"):
    print("Termina com c")

palavra = "bc"

if palavra in texto:
    print(palavra, "está em", texto)
print('\n')

print('SPLIT: Transformando string em lista')
texto = "A bc def"
lista = texto.split(" ")
print (lista)

texto = '111.222.333-44'
lista1 = texto.split('-')
print(lista1)
lista2 = lista1[0].split('.')
print(lista2)
print('\n')

print('JOIN: Transformando LISTA de string em String')
lista=['A','B','C']
juncao = ' depois de '
novaString = juncao.join(lista)
novastring2 =' '.join(lista)
print("Lista =", lista)
print("Texto =", novaString)
print("Final =",novastring2)


