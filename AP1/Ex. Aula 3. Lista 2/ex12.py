print('Escolha uma das opções: Soma, Diferença, Produto ou Divisão: ')
opcao = input('Digite a opção escolhida: ')
if opcao == 'soma' or opcao == 'diferença' or opcao == 'produto' or opcao == 'divisao':
    print('Opção valida!')

    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    if opcao == 'soma':
        print('Soma: ', num1 + num2)
    elif opcao == 'diferença':
        print('Diferença: ', num1 - num2)
    elif opcao == 'produto':
        print('Produto: ', num1 * num2)
    elif opcao == 'divisao' and num2 > 0:
        print('Divisão: ', num1 / num2)
    else:
        print('Não pode ser feita divisão por zero!')
else:
    print('Opção invalida!')
