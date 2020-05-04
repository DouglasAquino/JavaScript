s = 0
num = 500
sinal = -1
for cont in range(50):
    s = s + num * sinal
    num = num - 50
    sinal = sinal + 1
print(s)
