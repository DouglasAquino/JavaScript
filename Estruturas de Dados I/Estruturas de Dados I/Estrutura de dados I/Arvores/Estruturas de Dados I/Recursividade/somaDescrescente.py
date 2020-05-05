def somaDecrescente(n):
    if n==0:
        return 0
    else:
        return n + somaDecrescente(n-1)

print(somaDecrescente(10))
