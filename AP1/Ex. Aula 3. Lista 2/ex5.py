nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2)/2
print('Média: ', media)
if media < 3:
    print('Reprovado!')
elif media < 7:
    print('Vai para Exame!')
    exame = float(input('Nota do exame: '))
    notaFinal = (media + exame) / 2
    if notaFinal >= 6:
        print('Aprovado com exame!')
    else:
        print('Reprovado com exame!')
else:
    print('Aprovado!')
    
