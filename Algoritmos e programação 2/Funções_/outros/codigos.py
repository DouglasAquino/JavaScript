def leNota():
    return float(input('Digite a nota: '))
    
def calculaMedia(g1, g2):
    return round((g1 + 2 * g2)/3, 1)

def imprimeSit(mediaFinal):
    if mediaFinal >= 6:
        print('Com media: ', mediaFinal, 'Passou!')
    else:
        print('Com media:', mediaFinal, 'Reprovou!')
