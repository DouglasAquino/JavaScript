s = 0
sub = 100
for num in range(1, 51):
    s = s / (num - sub)
    sub = sub - 1
print(s)
