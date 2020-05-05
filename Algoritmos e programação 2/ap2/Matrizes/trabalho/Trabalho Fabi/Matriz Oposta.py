# Matriz Oposta
print('-----------------')
print('Matriz:')
matrizOposta = [[-10, 20, 30],
                [40, 50, 60],
                [70, 80, -90]]

for i in range(len(matrizOposta)):
     print(matrizOposta[i])
print('-----------------')
print('Matriz Oposta:')
for i in range(len(matrizOposta)):
     for j in range(len(matrizOposta)):
          matrizOposta[i][j] = matrizOposta[i][j] * -1
for i in range(len(matrizOposta)):
     print(matrizOposta[i])
