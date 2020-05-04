salMim = float(input('Salario minimo: '))
cont = 0
maiorSal = 0
salTotal = 0
while cont < 150:
    nome = input('Nome do funcionario: ')
    qtFilhos = int(input('Quantidade de filhos: '))
    nivel = input('Nivel estudado: ')
    cont = cont + 1
    if nivel == 'fundamental':
        salario = salMim + qtFilhos * 100
    elif nivel == 'medio':
        salario = (salMim * 3) + (qtFilhos * 100)
    else:
        salario = (salMim * 5) + (qtFilhos * 100)
    print('Nome: ', nome, 'Salario R$', salario)
    if salario > maiorSal:
        maiorSal = salario
    salTotal = salTotal + salario
print('Valor total dos salarios: ', salTotal)
print('Valor do maior salario: ', maiorSal)
