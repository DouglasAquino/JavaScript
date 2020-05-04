NotaProva = float(input('Nota da prova: '))
Trabalho = input('Fez o trabalho: ')
frequencia = int(input('Frequencia: '))

if frequencia >= 15 and Trabalho == 'sim':
    NotaFinal = NotaProva + 2 + 1
elif frequencia >= 15 and Trabalho == 'nao':
    NotaFinal = NotaProva + 1
elif frequencia < 15 and Trabalho == 'sim':
    NotaFinal = NotaProva
else:
    NotaFinal = NotaProva
print('Nota Final: ', NotaFinal)
