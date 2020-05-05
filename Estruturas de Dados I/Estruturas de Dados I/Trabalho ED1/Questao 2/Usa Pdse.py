import Pdse

p = Pdse.Pdse()
j = Pdse.Pdse()

p.insereInicio('a')
p.insereInicio('a')
p.insereInicio('b')
p.insereInicio('d')
p.insereInicio('c')
p.insereInicio('ah')
p.insereInicio('qr')
p.insereInicio('bg')
p.insereInicio('a')
p.show()
print("###"*15)

while p.getPrim() != 'c':
    j.insereInicio(p.getPrim())
    p.removerInicio()
p.removerInicio()
while p.estahVazia() == False:
    if p.getPrim() == j.getPrim():
        p.removerInicio()
        j.removerInicio()
        print('valor igual a xCy')
    else:
        p.removerInicio()
        j.removerInicio()
        print('valor diferente de xCy')
