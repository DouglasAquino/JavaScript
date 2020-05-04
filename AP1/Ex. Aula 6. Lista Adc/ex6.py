qtAlunos = int(input('Quantidade de alunos: '))
cont = 0
ausencia = 0
while cont < qtAlunos:
    matricula = int(input('Numero da matricula: '))
    chamada = input('A ou P: ')
    if chamada == 'a':
        ausencia = ausencia + 1
    cont = cont + 1
print('Percentual de ausencia: ', ausencia * 100 /qtAlunos)
