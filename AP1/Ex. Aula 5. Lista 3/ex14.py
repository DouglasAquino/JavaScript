cod = int(input('Digite o codigo: '))
refri = 0
suco = 0
agua = 0
while cod != 0:
    qt = int(input('Quantidade consumida: '))
    if cod == 100:
        refri = refri + qt
    elif cod == 101:
        suco = suco + qt
    elif cod == 102:
        agua = agua + qt
    else:
        print('Codigo nao registrado!')
    cod = int(input('Digite o codigo: '))
print('Quantidade de refrigerante: ', refri)
print('Total da compra: ', refri * 3 + suco * 4 + agua * 2)
