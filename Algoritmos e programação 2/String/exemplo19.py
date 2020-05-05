texto = input("Digite um texto: ")

if texto.isalpha():
    print("O texto contém somente letras")
elif texto.isdigit():
    print("O texto contém somente números")
elif texto.isalnum():
    print("O texto contém somente letras ou números")
