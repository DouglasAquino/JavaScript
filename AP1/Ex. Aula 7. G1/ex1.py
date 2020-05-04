tentativa = 1
senha = input('Digite a senha: ')
while senha != 'algoritmos1':
    print('Senha invalida!')
    tentativa = tentativa + 1
    senha = input('Digite a senha novamente: ')
print('Senha correta. {} tentativas!'.format(tentativa))
