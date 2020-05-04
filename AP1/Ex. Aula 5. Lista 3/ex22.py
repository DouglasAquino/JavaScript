cod = int(input('Código da turma: '))
qtAlunos = 0
maiorQtAlunos = 0
while cod > 0:
    turno = input('Turno da Turma: ')
    vagas = int(input('Quantidade de vagas ofertadas: '))
    alunos = int(input('Quantidade de alunos matriculados: '))
    if vagas == alunos:
        print('Preencheu as vagas!')
    else:
        print('Não preencheu as vagas!')
    qtAlunos = qtAlunos + alunos
    if alunos > maiorQtAlunos:
        maiorQtAlunos = alunos
        codTurma = cod
    cod = int(input('Código da turma: '))
print('Quantidade de alunos matriculados: ', qtAlunos)
print('Codigo da turma com maior quantidade de alunos: ', codTurma)
