'''Um professor passou uma lista com 10 exercícios para cada um de 6 alunos e mediu o tempo que cada aluno levou para fazer cada exercício. 
Faça um programa (a – valor 1,0) que (b – valor 1,0) leia os nomes e os tempos (em minutos inteiros, sem os segundos)
de cada exercício de cada aluno e guarde as informações em uma matriz. Ao final, o programa deve informar: 
(c – valor 1,0) Qual o aluno que respondeu mais rápido a um exercício, e qual foi o exercício (se foi o 1º, o 2º e assim por diante).
Considere que não houve empate.(d – valor 1,0) Qual foi o aluno que demorou mais a responder a todos os exercícios.
Os itens de “b” a “d” devem ser implementados como funções em um módulo que deve ser chamado (importado) pelo programa principal
(que é o item a, caso não tenha percebido ali acima)
Serão considerados na avaliação: a correta implementação das funções, o uso adequado de nomes das funções, as passagens de argumentos e os retornos.'''


def le_nomes_e_tempos():
     matriz = []
     for i in range(3):
          linha = []
          nome = input('Digite o Nome do Aluno: ')
          linha.append(nome)
          for i in range(5):
               tempo = int(input('Digite o Tempo gasto em cada exercicio: '))
               linha.append(tempo)
          matriz.append(linha)
     return matriz

def mais_rapido(lista_alunos):
     menor = 100
     for i in lista_alunos:
          if min(i[1:]) < menor:
               menor = min(i[1:])
               nome = i[0]
     string = str(menor)
     converter_string = []
     for i in lista_alunos:
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
     return f'O melhor tempo foi do(a): {nome} em: {menor} segundos. \nO/A aluno(a): {indice[0]} fez o melhor tempo no exercicio: {indice[1]}.'


def mais_lento(lista_alunos):
     soma = []
     for i in lista_alunos:
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
     return f'O mais lento foi {nome}, com o tempo total de {maior} segundos.'





