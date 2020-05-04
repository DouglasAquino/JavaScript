nome = input('Nome do hotel: ')
maiorDist = 0
visitaMed = 0
while nome != 'sair':
    distCentro = float(input('Distancia do centro: '))
    visita = int(input('Numero de visitantes: '))
    acesso = int(input('Acesso 0 ou acesso 1: '))
    if distCentro > 15:
        maiorDist = maiorDist + 1
        print('Hotel distantes á maios que 15KM: ',nome, distCentro)
    if acesso == 0:
        visitaMed = visitaMed + visita
    if visita < 1000 and acesso == 1:
        print('Distancia: ', distCentro, 'Visitantes: ', visita)
    if distCentro > maiorDist:
        maiorDist = distCentro
        nomeDist = nome
    nome = input('Nome do hotel: ')

print('Quantidade de visitantes: ', visitaMed)
print('Mais Distante: ', nomeDist)
