s = 0
n = int(input('Valor de N: '))
x = int(input('Valor de X: '))
for num in range(1, n + 1):
    fat = 1
    for val in range(num, 0, -1):
        fat = fat * val
    s = s + fat / x
print(s)
