import PilhaD
p=PilhaD.PilhaD()
palavra="((5+3-2))"
for i in palavra:
    if i=="(":
        p.push("(")
    elif i==")":
        if p.estahVazia()==False:
            p.pop()
        else:
            print("Parentese de fechamento a mais")
    if not p.estahVazia():
        print("Parentese de abertura a mais")
