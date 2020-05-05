import Les
l1=Les.Les()
l2=Les.Les()

#print(l1.estahVazia())#ver se a lista está vazia
#print(l1.estahCheia())

if not l1.estahCheia():
   l1.inserirFim('A')
if not l1.estahCheia():
   l1.inserirFim('B')

#l1.show()

if not l1.estahVazia():
    l1.removerFim()

#l1.show()

l1.inserirFim('D')

#l1.show()

l1.inserirInicio('A')
l1.inserirInicio('B')
l1.inserirInicio('C')
#l1.show()


l2.inserirInicio(l1.getPrim())
l1.removerInicio()
l2.inserirInicio(l1.getPrim())
l1.removerInicio()
l2.inserirInicio(l1.getPrim())
l1.removerInicio()
#l1.show()
#l2.show()
'''
if l1.estahVazia():
   print('L1 vazia')
else:
   print('L1 tem elemento')
'''

'''
if l2.estahVazia():
   print('L2 vazia')
else:
   print('L2 tem elemento')
'''
'''
l1.inserirFim('F')
l1.inserirInicio('D')
#l1.show()
l1.inserirAposDet('D','F')
#l1.show()
'''

#l2.show()
l2.removerInicio()
l2.inserirFim('B')
#l2.show()
l2.inserirAposDet('E','B')
l2.show()



