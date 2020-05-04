maiorSal = 0
somaSal = 0
salMim = float(input('Salario Minimo: '))
nome = input('Nome: ')
while nome != 'sair':
    qtPecas = int(input('Quantidade de peças: '))
    if qtPecas <= 100:
        salario = salMim + qtPecas * 1
        print('O funcionario {} recebe R${} e está na categoria A'.format(nome, salario))
    else:
        salario = salMim + qtPecas * 1.50
        print('O funcionario {} recebe R${} e está na categoria B'.format(nome, salario))
    somaSal = somaSal + salario
    if salario > maiorSal:
        maiorSal = salario
    nome = input('Nome: ')
print('O valor do maior salario é R$', maiorSal)
print('A somatoria dos salarios é R$', somaSal)
