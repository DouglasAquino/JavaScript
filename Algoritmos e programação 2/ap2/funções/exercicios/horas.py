'''7.	Faça uma função que recebe como argumento o tempo representado em segundos e retorne esse tempo em horas, minutos e segundos.
A hora completa deve ser retornada em uma variável no seguinte formato “Horas:Minutos:Segundos”,
por exemplo, se for passado como argumento 3800 segundos para o método, este deverá retornar “1:3:20”, que indica, 1 hora, 3 minutos e 20 segundos.
ATENÇÃO: Para formatar a variável de retorno, você precisará converter os valores para string.
Para isso, utilize a função str(), que recebe um número inteiro como argumento e o converte para string. '''

def converter(segundos):
     lista = []
     lista.append(segundos // 3600)
     restantes = segundos % 3600
     lista.append(restantes // 60)
     lista.append(restantes % 60)
     
     lista1 = ':'.join(map(str, lista))

     return lista1
     
     
     
