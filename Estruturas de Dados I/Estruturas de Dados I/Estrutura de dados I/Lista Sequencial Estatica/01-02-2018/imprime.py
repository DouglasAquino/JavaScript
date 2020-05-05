import Palavra
p= Palavra.Palavra()
p.insereLetra('A')
p.insereLetra('B')
p.imprimePalavra()
print('\n')
p.removeLetra()
p.imprimePalavra()
print('\n')
p.insereLetra('C')
p.imprimePalavra()
print('\n')
p.insereLetraInicio('D')
#DAB
p.imprimePalavra()
p.removeLetraInicio()
#AB
p.imprimePalavra()

if not p.palavraCheia():
    p.insereLetra('D')
else:
    print('esta cheia')
