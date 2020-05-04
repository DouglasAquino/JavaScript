horario = float(input('Quantidade de hora aula: '))
titulacao = input('Titulação: ')
if titulacao == 'especialista':
    print('Salário de um Especialista: ', horario * 30 * 4.5)
elif titulacao == 'mestre':
    print('Salário de um Mestre: ', horario * 45 * 4.5)
else:
    print('Salario de um Doutor: ', horario * 60 * 4.5)
