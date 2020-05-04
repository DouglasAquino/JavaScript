maiorNota = 0
cont = 0
while cont < 3:
    nome = input('Nome: ')
    nota = float(input('Nota: '))
    if nota > maiorNota:
        maiorNota = nota
        nomepri = nome
    cont = cont + 1
print('Maior nota: ', maiorNota, 'Primeiro colocado: ', nomepri)
