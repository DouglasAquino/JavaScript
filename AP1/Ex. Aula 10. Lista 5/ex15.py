s = 0
for num in range(10, 1, -2):
    fat = 1
    for val in range(num, 0, -1):
        fat = fat * val
    s = s + fat
print(s)
