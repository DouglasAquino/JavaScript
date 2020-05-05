print('Listas')
print('Com listas podemos manipular os dados nas posições já existentes')
listaDeDados = ['0', 1 ,'2', 3 ,'   4',5]
print (listaDeDados[1])
listaDeDados[1] = "numero"
print (listaDeDados[1])
print(listaDeDados)

print('------------------------------------------------------------------')

print('Mas... Nada de extrapolar! (lembrando: nas posições já existentes)')
print()
'''
listaDeDados = ['0', 1 ,'2', 3 ,'   4',5]
print (listaDeDados[6]) #também não pode extrapolar
'''
print('------------------------------------------------------------------')

# LISTAS – um pouco mais
print('Trabalhando com a Lista')
print('Criando Lista vazia')
listaVazia = []
print('Criando Lista com somente um valor')
listaComUm = ['um']
print('Tamanho da Lista: len')
print (len (listaVazia))
print (len (listaComUm))

print('------------------------------------------------------------------')

print('append(x)  -- insere x no fim da lista')
lista1 = ["a", "b", "c"]
print ("lista1 antes do append:", lista1)
lista1.append("f")
print ("lista1 depois do append:", lista1)

print('------------------------------------------------------------------')

print('append(x)  -- e se eu inserir uma lista x no fim da lista?')
lista1 = ["a", "b", "c"]
lista2 = ["d", "e"]
print ("lista1 antes do append:", lista1)
lista1.append(lista2)
print ("lista1 depois do append:", lista1)

print('------------------------------------------------------------------')

print('extend (L)  -- insere a lista L no fim da lista original')
lista1 = ["a", "b", "c"]
lista2 = ["d", "e"]
print ("lista1 antes do extend:", lista1)
lista1.extend(lista2)
print ("lista1 depois do extend:", lista1)

print('----------------------------------------------------------------------')


print('insert(i, x)  -- insere x na posição i')
print('O primeiro argumento é o índice em que será feita a inserção')
lista1 = ["a", "b", "c"]
print ("lista1 antes do insert:", lista1)
lista1.insert(2,"k")
print ("lista1 depois do insert:", lista1)

print('------------------------------------------------------------------------')

print('remove(x)  -- remove o primeiro item encontrado na lista cujo valor é igual a x. Se não existir valor igual, uma exceção ValueError é levantada. ')
lista1 = ["a", "b", "c"]
print ("lista1 antes do remove:", lista1)
lista1.remove("b")
print ("lista1 depois do remove:", lista1)
# erro
'''
lista1 = ["a", "b", "c"]
print ("lista1 antes do remove:", lista1)
lista1.remove("f")
print ("lista1 depois do remove:", lista1)
'''
print('-------------------------------------------------------------------------')

print('pop(i)  -- Remove o item na posição dada e o retorna. Se nenhum índice for especificado, \n o comando remove e retorna o último item na lista. i é opcional')
lista1 = ["a", "b", "c"]
print ("lista1 antes do pop:", lista1)
x = lista1.pop(1)
print ("lista1 depois do pop:", lista1)
print ("Valor de x:", x)

print('-------------------------------------------------------------------------')

print('pop(i)  -- testando sem o i')
lista1 = ["a", "b", "c"]
print ("lista1 antes do pop:", lista1)
x = lista1.pop()
print ("lista1 depois do pop:", lista1)
print ("Valor de x:", x)

print('-------------------------------------------------------------------------')

print('index(x)  -- retorna o índice do primeiro item cujo valor é igual a x, gerando a exceção ValueError se o valor não existir')
lista1 = ["a", "b", "c"]
indice = lista1.index("b")
print ("indice=", indice)

print('-------------------------------------------------------------------------')

print('count(x)  -- devolve o número de vezes que o valor x aparece na lista.')
lista1 = ["a", "b", "c", "b"]
print ("Quantidade de \"b\" =", lista1.count("b"))
print ("Quantidade de \"t\" =", lista1.count("t"))

print('-------------------------------------------------------------------------')

print('sort()  -- ordena os itens na própria lista.')
lista1 = ["x", "b", "v", "b"]
print ("lista1 antes do sort:", lista1)
lista1.sort()
print ("lista1 depois do sort:", lista1)

print('-------------------------------------------------------------------------')

print('reverse()  -- inverte a ordem dos elementos na lista.')
lista1 = ["x", "b", "v", "b"]
print ("lista1 antes do reverse:", lista1)
lista1.reverse()
print ("lista1 depois do reverse:", lista1)

print('-------------------------------------------------------------------------')

print('Listas - Cuidados')
lista1 = ["a", "b", "c"]
lista2 = lista1
print ("lista1 antes do append:", lista1)
print ("lista2 antes do append", lista2)
lista1.append("******")
print ("lista1 depois do append:", lista1)
print ("lista2 depois do append", lista2)
lista2[0]="Abracadabra"
print ("lista1 depois da atribuição:", lista1)
print ("lista2 depois da atribuição", lista2)

print('-------------------------------------------------------------------------')

print('O operador [a:b] possui o comprimento de a (inclusive) até b(exclusive)')
print('O operador [:b] possui o comprimento até b (exclusive)')
print('O operador [a:] possui o comprimento a partir de a (inclusive)')
lista = ['a','b','c','d','e']
print(lista[1:4])
print(lista[2:])
print(lista[:2])
print(lista)
print(lista[0:5])
print(lista[:5])
print(lista[:])
print(lista[-3:4])
print(lista[-3:-1])

print('-------------------------------------------------------------------------')

print('O operador [a:b:salto] possui o comprimento de a (inclusive) até b (exclusive) de n em n posições')
lista = ['a','b','c','d','e']
print(lista[1:5:2])
print()

lista = ["CEULP", 5, "23", 100]
nova = lista[:2]
print ("Mudança 1:", nova)
nova = lista[2:]+["a",3*10]
print ("Mudança 2:", nova)
nova = 3*lista[:3]
print ("Mudança 3:", nova)
print()

lista = ["CEULP", 5, "23", 100]
print ("Antes da mudança 1:", lista)
lista[0:2]=["a","b"]
print ("Depois da mudança 1:", lista)
lista[0:2]=["c"]
print ("Depois da mudança 2:", lista)
lista[0:2]=["d", "e", "f"]
print ("Depois da mudança 3:", lista)

print('-------------------------------------------------------------------------')

print('len(lista)  -- retorna o tamanho da lista')

print('-------------------------------------------------------------------------')

print('del  -- remove o elemento pelo índice sem retorná-lo. Atente-se que a sintaxe muda. Permite eliminar slices também')
lista1 = ["x", "b", "v", "b"]
print ("lista1 antes do del:", lista1)
del lista1[1]
print ("lista1 depois do primeiro del:", lista1)
del lista1[0:2]
print ("lista1 depois do segundo del:", lista1)

print('-------------------------------------------------------------------------')

print('max(lista)  -- retorna o maior valor da lista')
print('min(lista)  -- retorna o maior valor da lista')
lista = ['C','e','c','D','E']
print(max(lista))
print(min(lista))

print('-------------------------------------------------------------------------')

print('sorted(lista)  -- retorna a lista com os valores em ordem crescente')
lista = ['C','e','c','D','E']
print(lista)
print(sorted(lista))
print(lista)
lista=sorted(lista)
print(lista)

print('--------------------------------------------------------------------------')

print('reversed(lista)  -- retorna um iterador para percorrer os elementos do último ao primeiro')
lista = ['C','e','c','D','E']
print(reversed(lista))
for i in reversed(lista):
    print(i)
lista = reversed(lista)
print(lista)

print('--------------------------------------------------------------------------------')

print('Listas aninhadas')
a = ["pa", "q", "r"]
b = ["t", a, "u"]
print ("b:", b)
print ("b[1]:", b[1])
print ("b[1][0]:", b[1][0])

print('------------------------------------------------------------------------------------')

print('Tuplas')
print('Da mesma forma que Lista, basta dar um nome e atribuir valores a ela, porém usando parênteses...')
meses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho',\
'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
print (meses[0:2])
novoMeses = meses[0:2]
print (novoMeses)
print()

print('Trabalhando com os valores da Tupla')
dados = ('0', 1 ,'2', 3 ,'   4',5) #também funciona sem parênteses

#print (dados[0] + dados[1])
print (dados[0] + str(dados[1]))
print (int(dados[0]) + dados[1])
print (dados[0] + dados[2])
print (dados[1] + dados[3])
print (dados[4])
print (dados[2] + dados[4])
#print (dados[6]) #tire o comentário e veja o que acontece


print('--------------------------------------------------------------------------------------')

print('Trabalhando com a Tupla')
print('Criando Tupla vazia')
dadosVazio = ()
print('Criando Tupla com somente um valor')
dadosUm = (1,)
print('Tamanho da Tupla: len')
print (len (dadosVazio))
print (len (dadosUm))
# dados[1]= 7



































































































































































