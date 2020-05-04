alturaChico = 1.40
ChicoCresce = 0.15
alturaZe = 1.10
ZeCresce = 0.25
anos = 0
while alturaZe < alturaChico:
    alturaChico = alturaChico + ChicoCresce
    alturaZe = alturaZe + ZeCresce
    print(alturaChico, alturaZe)
    anos = anos + 1
    if alturaZe > alturaChico:
        print('Daqui a {} anos!'.format(anos))
