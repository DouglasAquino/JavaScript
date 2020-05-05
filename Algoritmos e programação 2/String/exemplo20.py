texto = "abc"

if texto.startswith("a"):
    print("Começa com a")

if texto.endswith("c"):
    print("Termina com c")

palavra = "bc"

if palavra in texto:
    print(palavra, "está em", texto)
