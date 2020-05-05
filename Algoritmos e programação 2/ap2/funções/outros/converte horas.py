def converterHora(hora24, minuto24):
     if hora24 > 23 or hora24 < 0 or minuto24 < 0 or minuto24 > 59:
          return None
     if hora24 < 12:
          hora24 -= 12
          return  (hora24, minuto24)
     
     if hora24 > 12:
          hora24 -= 12
          return  (hora24, minuto24)

continuar = 's'

while continuar == 's':
     hora = int(input('Informe o valor da hora: '))
     minuto = int(input('Informe o valor dos minutos: '))

     print(converterHora(hora, minuto))

     continuar = input('Deseja continuar: ')
          
     
