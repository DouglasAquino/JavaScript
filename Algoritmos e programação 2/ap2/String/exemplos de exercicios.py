'''
Faça um programa que leia 2 strings e
informe o conteúdo delas seguido do
seu comprimento. Informe também se
as duas strings possuem o mesmo comprimento e são iguais ou diferentes
no conteúdo. 

s1 = input("String 1: ")
s2 = input("String 2: ")
print("Tamanho de s1: ", len(s1))
print("Tamanho de s2: ", len(s1))
if len(s1) == len(s2):
	print("Possuem tamanhos iguais")
else:
	print("Possuem tamanhos diferentes")
# O método lower () retorna uma cópia da string na qual todos os caracteres baseados em casos foram minúsculos.
if s1.lower() == s2.lower():
	print("São iguais")
else: 
	print("Mas diferentes")
'''


'''Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = ""
s = "" 
nome = input("Informe o nome:")
for letra in reversed(nome):
	s+=letra
print(s.upper())
'''

'''03- Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
nome = input("Informe o nome: ")
#print("\n".join(nome))
for letra in nome:
	print(letra)
'''

'''04 - Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada
#nome = input("Informe o nome: ")
nome= "ezequiel"
s = ""

for letra in nome:
     s+=letra
     print(s)
'''


'''09 - Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.'''



cpf = input("CPF(xxx.xxx.xxx-xx) :") #3 7 11


for letra in cpf:
	while(cpf[3] !=".") or (cpf[7] !=".") or (cpf[11] !="-"):
		cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")






















