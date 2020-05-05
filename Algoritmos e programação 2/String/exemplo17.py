frase = input("Digite uma palavra: ")

if frase.islower():
    print("A frase está toda em minúsculas")
elif frase.isupper():
    print("A frase está toda em maiúsculas")
elif frase.istitle():
    print("A frase tem somente as primeiras letras em maiúsculas ")
