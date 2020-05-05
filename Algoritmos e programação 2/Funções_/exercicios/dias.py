'''5.	Faça uma função que recebe a idade de uma pessoa em anos, meses e dias (um parâmetro para anos, outro para meses e outro para dias)
e retorne essa idade em dias. Considere que um ano tem 360 dias e os meses são de 30 dias. '''

def idade(ano, mes, dia):
     ano = ano * 360
     mes = mes * 30
     idade = dia + ano + mes
     return idade

'''
from dias import *

ano = int(input('Qual a sua idade: '))
mes = int(input('Quantos meses: '))
dia = int(input('Quantidade de dias: '))

print(idade(ano, mes, dia))
'''
