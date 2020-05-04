qtpopulacao = int(input('Quantidade de pessoas em 2017: '))
ano = 2017

while ano < 2050:
    qtpopulacao = qtpopulacao + qtpopulacao * 0.10
    ano = ano + 1
    print(ano, '---', qtpopulacao)
