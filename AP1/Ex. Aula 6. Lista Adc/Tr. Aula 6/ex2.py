from random import randint
computador = randint(0, 100)
jogar = input('Deseja jogar? ')
chute = 0
palpite = 0
if jogar == 'sim':
    print('Adivinha em que numero pensei? ')

while jogar == 'sim':
    palpite = int(input('Jogador, qual é o seu palpite? '))
    chute = chute + 1
    if palpite < computador:
        print('O palpite {} é menor do que o pensado!'.format(palpite))
    elif palpite > computador:
        print('O palpite {} é maior do que o pensado!'.format(palpite))
    else:
        print('*'*45)
        print('Meus parabéns! o numero que pensei foi: ', computador)
        print('Jogador voce acertou com {} chutes!'.format(chute))
        print('*'*45)
        jogar = input('Deseja jogar novamente? ')
        chute = 0
        computador = randint(0, 100)
