somaId = 0
qt = 0
qtMulher = 0
qtHomem = 0
while qt <10:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ')
    qt = qt + 1
    somaId = somaId + idade
    if sexo == 'feminino':
        qtMulher = qtMulher + 1
    else:
        qtHomem = qtHomem + 1
print('Média das idades: ', somaId / qt)
if qtMulher > qtHomem:
    print('Há mais mulheres!')
elif qtHomem > qtMulher:
    print('Há mais homens!')
else:
    print('Mesma quantidade!')
