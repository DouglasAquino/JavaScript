horas = int(input('Horas jogando LoL: '))
if horas >= 0 and horas <= 24:
    print('Horario valido!')
    if horas <= 2:
        print('Nunca será um bom jogador, mas será um bom aluno!')
    elif horas <= 4:
        print('Trá dificuldades nas matérias, mas será um bom jogador!')
    elif horas <= 6:
        print('Vai demoras a se formar, mas ficará bom no jogo!')
    else:
        print('Seu cerebro vai começar a derreter, mas será um excelente jogador!')
else:
    print('Horario invalido!')
