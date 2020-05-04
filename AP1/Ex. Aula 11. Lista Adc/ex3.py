s = 0
den = 3
for num in range(5, 101, 5):
    s = s + num/den
    den = den + 5
print(s)
