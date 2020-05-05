'''Uma pista de Kart permite 10 voltas para cada um de 6 corredores. 
Faça um programa (a – valor 1,0) que (b – valor 1,0) leia os nomes e os tempos (em segundos) de cada volta
de cada corredor e guarde as informações em uma matriz. Ao final, o programa deve informar: 
(c – valor 1,0) De quem foi a melhor volta da prova, e em que volta (se foi a 1º, a 2º e assim por diante).
Considere que não houve empate.
(d – valor 1,0) Qual foi o corredor que, no total, foi mais lento na soma de todas voltas.
Os itens de “b” a “d” devem ser implementados como funções em um módulo que deve ser chamado
(importado)pelo programa principal (que é o item a, caso não tenha percebido ali acima)
Serão considerados na avaliação: a correta implementação das funções,
o uso adequado de nomes das funções, as passagens de argumentos e os retornos.'''



def le_corredores_e_tempo():
     matriz = []
     for i in range(3):
          linha = []
          nome = input('Digite o Nome: ')
          linha.append(nome)
          for i in range(5):
               tempo = int(input('Digite o Tempo: '))
               linha.append(tempo)
          matriz.append(linha)
     return matriz

def melhor(lista_corredores):
     print(lista_corredores)

     menor = 100

     for i in lista_corredores:
          if min(i[1:]) < menor:
               menor = min(i[1:])
               nome = i[0]


     string = str(menor)
     converter_string = []
     for i in lista_corredores:
          linha = []
          for x in range(len(i)):
               linha.append(str(i[x]))
          converter_string.append(linha)
     indice = []
     for i in converter_string:
          for x in range(len(i)):
               if i[x] == string:
                    indice.append(i[0])
                    indice.append(x)
     return f'A melhor volta foi do(a): {nome} em: {menor} segundos. \nA corredora: {indice[0]} fez o melhor tempo na volta: {indice[1]}.'

def mais_lento(lista_corredores):
     soma = []
     for i in lista_corredores:
          linha = []
          linha.append(i[0])
          soma_linha = sum(i[1:])
          linha.append(soma_linha)
          soma.append(linha)
     maior = 0
     nome = ''
     for i in soma:
          if i[1] > maior:
               maior = i[1]
               nome = i[0]


     return f'O mais lento foi {nome}, com o tempo de {maior} segundos.'











          



 
