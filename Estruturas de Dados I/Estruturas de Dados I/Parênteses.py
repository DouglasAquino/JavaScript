import PILHA as P

P1 = P.Pilha()

entrada = input("Digite: ")

for c in entrada:
    if c == "(":
        P1.push(c)
    elif c == ")":
        if P1.estahVazia():
            print("Erro")
            break
        else:
            P1.pop()

if P1.estahVazia() == False:
    print("Erro")

