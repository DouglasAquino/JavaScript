s = 0
sinal = -1
for num in range(2, 21, 2):
    s = s + num / (num / 2 * sinal)
    sinal = sinal * -1
print(s)
