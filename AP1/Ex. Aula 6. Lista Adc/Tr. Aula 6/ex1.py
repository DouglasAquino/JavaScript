tPadrao1 = float(input('Tempo padrão 1: '))
tPadrao2 = float(input('Tempo padrão 2: '))
tPadrao3 = float(input('Tempo padrão 3: '))
calculo = 0
vencedor = 0
inscVencedora = 0
inscricao = int(input('Númeo de inscrição: '))
while inscricao != 9999:
    tEtapa1 = float(input('Tempo etapa 1: '))
    c1 = tEtapa1 - tPadrao1
    if c1 < 3:
        calculo = calculo + 100
    elif c1 >= 3 and c1 <= 5:
        calculo = calculo + 80
    else:
        calculo = 80-((c1 - 5)/5)

    tEtapa2 = float(input('Tempo etapa 2: '))
    c2 = tEtapa2 - tPadrao2
    if c2 < 3:
        calculo = calculo + 100
    elif c2 >= 3 and c2 <= 5:
        calculo = calculo + 80
    else:
        calculo = 80-((c2 - 5)/5)

    tEtapa3 = float(input('Tempo etapa 3: '))
    c3 = tEtapa3 - tPadrao3
    if c3 < 3:
        calculo = calculo + 100
    elif c3 >= 3 and c3 <= 5:
        calculo = calculo + 80
    else:
        calculo = 80-((c3 - 5)/5)

    print('Total de pontos: ', calculo)
    if calculo > vencedor:
        vencedor = calculo
        inscVencedora = inscricao
    inscricao = int(input('Númeo de inscrição: '))
    calculo = 0
print('Numero da equipe vencedora: ', inscVencedora)
