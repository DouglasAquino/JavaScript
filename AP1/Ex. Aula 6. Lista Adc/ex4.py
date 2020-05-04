preco = float(input('Preço do produto: '))
maiorPreco = 0
menorPreco = 99999999
while preco > 0:
    nome = input('Nome do Artista: ')
    categoria = input('Categoria: Quadro ou Escultura: ')
    if preco > maiorPreco and categoria == 'escultura':
        maiorPreco = preco
        nomeArtista = nome
    elif preco < menorPreco:
        menorPreco = preco
        categoriaBarata = categoria
    preco = float(input('Preço do produto: '))
print('Nome do artista da categoria escultura mais cara: ', nomeArtista)
print('Categoria mais barata: ', categoriaBarata)
