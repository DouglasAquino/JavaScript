x = 0
y = 0
for num in range(50, 1001, 50):
    x = x + num
for nnum2 in range(1, 21):
    y = y + x * num
print('Z: ', y/x)
