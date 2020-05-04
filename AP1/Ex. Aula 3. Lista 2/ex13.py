HoraEntrada = int(input('Hora de Entrada: '))
HoraSaida = int(input('Hora Saida: '))
if HoraEntrada >= HoraSaida or HoraEntrada < 10 or HoraEntrada > 22 or HoraSaida < 10 or HoraSaida > 22:
    print('Horario Invalido!')
else:
    tempo = HoraSaida - HoraEntrada
    if tempo == 1:
        print('Valor R$4.00!')
    elif tempo == 2:
        print('Valor R$6.00!')
    else:
        tempoadicional = tempo - 2
        valor = 6 +(tempoadicional * 1)
        print('Valor R$', valor)
