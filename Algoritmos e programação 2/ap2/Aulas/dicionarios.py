contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'), ('Ana', '8765-4321'), ('Marina', '1111-1111')]

# DICT cria um dicionario
contatos = dict(contatos_lista)
print(contatos)

# Encontrar um contato esxistente
print('-'*33)
print(contatos['Ana'])
print('-'*33)

# Encontrar um contato esxistente e não existente
print(contatos.get('Yan', 'Contato não encontrado'))
print(contatos.get('João', 'Contato não encontrado'))
print('-'*33)
print('Yan' in contatos)
print('-'*33)

# Encontrar atraves do contato e nao do nome
print('9999-9999' in contatos.values())
print('-'*33)

# Adicionar elementos no dicionario
contatos['João'] = '8889-7778'
print(contatos)
print('-'*33)

# Remover itend do dicionario
# Quando existe
del contatos['Marina']
print(contatos)
print('-'*33)
# Quando nao existe
print(contatos.pop('Ana', 'Contato não encontrado'))
print(contatos.pop('Catarina', 'Contato não encontrado'))
print(contatos)
print('-'*33)

# Juntando dois dicionarios
contatos_pedro = {'Yan': '1234-5678', 'Pedro': '9999-9999', 'João': '8889-7778'}
meus_contatos = {'Wesley': '2356-5678', 'Breno': '9119-9999', 'Martha': '0000-7778'}
for nome in contatos_pedro:
     meus_contatos[nome] = contatos_pedro[nome]
print(meus_contatos)
print('-'*50)

meus_contatos.update(contatos_pedro)
print(meus_contatos)
print('-'*50)

# Adicionar o prefixo 9
meus_contatos_novo = {nome: '9' + meus_contatos[nome] for nome in meus_contatos}
print(meus_contatos_novo)












