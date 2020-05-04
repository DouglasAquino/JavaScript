salMim = float(input('Salario minimo: '))
cont = 0
setorC = 0
nomSal = 0
maiorSal = 0
while cont < 3:
    nome = input('Nome do Vendedor: ')
    setor = input('Setor de vendas: ')
    vendas = float(input('Valor de vendas: '))
    sal = salMim + vendas * 0.08
    print('Vendedor {}, Recebe o salario de R${}'.format(nome, sal))
    if setor == 'calçados' and vendas >= 5000 and vendas <= 10000:
        setorC = setorC + 1
    if sal > maiorSal:
        maiorSal = sal
        nomSal = nome
    cont = cont + 1
print('Quantidade de vendedores do setor C que venderam entre R$5000.00 e R$10000.00: ', setorC)
print('Quem recebeu o maior salario foi: ', nomSal)
