fichas = int(input('Ficha do candidato: '))
cand1 = 0
cand2 = 0
cand3 = 0
branco = 0
nulo = 0
cont = 0
while fichas != 0:
    if fichas == 1:
        cand1 = cand1 + 1
    elif fichas == 2:
        cand2 = cand2 + 1
    elif fichas == 3:
        cand3 = cand3 + 1
    elif fichas == 4:
        branco = branco + 1
    else:
        nulo = nulo + 1
    cont = cont + 1
    fichas = int(input('Ficha do candidato: '))
print('Quantidade de eleitores: ', cont)
print('Não escolheram candidatos: ', nulo + branco)
if cand1 > cand2 and cand1 > cand3:
    print('O candidato 1 é o vencedor!')
elif cand2 > cand1 and cand2 > cand3:
    print('O candidato 2 é o vencedor!')
else:
    print('O candidato 3 é o vencedor!')
    
