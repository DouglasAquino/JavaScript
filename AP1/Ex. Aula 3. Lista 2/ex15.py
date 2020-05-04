QtLivros = int(input('Quantidade de livros: '))
A = 0.5 * QtLivros + 10
B = 0.8 * QtLivros + 5

if A == B:
    print('As duas opções oferecem o mesmo desconto!')
elif A > B:
    print('A melhor opção de desconto é o Critério A!')
else:
    print('A melhor opção de desconto é o Critério B!')
