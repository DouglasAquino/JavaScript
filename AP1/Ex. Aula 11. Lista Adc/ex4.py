s = 0
num = 480
den = 10
sinal = 1
for cont in range(30):
    s = s + num * sinal/den
    num = num - 5
    den = den + 1
    sinal = sinal * -1
print(s)
