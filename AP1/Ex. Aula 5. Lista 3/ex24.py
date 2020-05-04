canal = int(input('Canal 4 ou 5? '))
qtCasas = 0
pessoas = 0
while canal != 0:
    qtPessoas = int(input('Quantidade de pessoas que assistem: '))
    if canal == 4:
        qtCasas = qtCasas + 1
    else:
        pessoas = pessoas + qtPessoas
    canal = int(input('Canal 4 ou 5? '))
print('Quantidade de casas que assistem ao canal 4: ', qtCasas)
print('Quantidade de pessoas que assistem ao canal 5: ', pessoas)
