import Tree
t1 = Tree.Tree()

t1.insere(55)
t1.insere(48)
t1.insere(50)
t1.insere(35)
t1.insere(51)
t1.insere(70)
t1.insere(60)
t1.insere(90)
t1.insere(65)

print("IN-ORDEM:")
t1.inOrdem()
print("\nPRE-ORDEM:")
t1.preOrdem()
print("\nPOS-ORDEM:")
t1.posOrdem()
