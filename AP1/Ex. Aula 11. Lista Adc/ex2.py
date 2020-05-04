num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
if num1 > num2:
    for i in range(num1-1, num2, -1):
        print(i)
else:
    for i in range(num1+1, num2, 1):
        print(i)
