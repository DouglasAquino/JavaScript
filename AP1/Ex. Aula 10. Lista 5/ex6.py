s = 0
x = int(input('Número: '))
for num in range(10, 5001, 10):
    s = s + num * x
s = s / 100
print('Soma: ', s)
