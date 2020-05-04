alunos = int(input('Quantidade de alunos: '))
cont = 0
med = 0
while cont < alunos:
    media = float(input('Média: '))
    med = med + media
    cont = cont + 1
print('Média aritmetica: ', med / alunos)
