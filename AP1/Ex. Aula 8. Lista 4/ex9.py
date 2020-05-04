G = []
R = []
acertos = 0
i = 0
while i < 10:
    G.append(input('Gabarito: '))
    i = i + 1
print('Gabarito: ', G)
i = 0
while i < 10:
    R.append(input('Respostas: '))
    i = i + 1
print('Respostas: ', R)
i = 0
while i < 10:
    if G[i] != R[i]:
        print('Errou a: ', i)
    else:
        acertos = acertos + 1
    i = i + 1
if acertos >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')
