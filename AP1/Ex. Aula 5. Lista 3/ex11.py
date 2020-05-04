A = 1000
B = 500
ano = 0
while B < A:
    A = A + 100
    B = B + 130
    print(A, B)
    ano = ano + 1
    if B > A:
        print('Daqui a {} anos!'.format(ano))
