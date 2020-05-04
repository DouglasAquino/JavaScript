cont = 0
infantil = 0
fund = 0
maiorMedia = 0
while cont < 3:
    nivel = input('Nivel estudado: ')
    qtLivros = int(input('Quantidade de livros: '))
    repete = input('Le o livro mais de uma vez: ')
    if nivel == 'infantil' and qtLivros < 3:
        infantil = infantil + 1
    if nivel == 'fundamental' and qtLivros > 3 and qtLivros <= 6:
        fund = fund + 1
    if nivel == 'medio':
        if qtLivros > maiorMedia:
            maiorMedia = qtLivros
    cont = cont + 1
print('Infantil que le menos de 3 livros: ', infantil)
print('Fundamental que le entre 3 e 6: ', fund)
print('Mais lido no ensino medio: ', maiorMedia)
