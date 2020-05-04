den = 10
s = 0
for num in range(200, 10, -10):
    s = s + num / den
    den = den + 1
print(s)
