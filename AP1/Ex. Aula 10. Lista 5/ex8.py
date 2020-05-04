fat = 1
num = int(input('Número: '))
for x in range(num, 0, -1):
    fat = fat * x
print('Fatorial: ', fat)
