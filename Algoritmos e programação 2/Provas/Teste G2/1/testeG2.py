def fazAlgo(*a):
    valor = a[0]
    i = 1
    while i < len(a):
        valor = valor/a[i]
        i += 1
    return valor

def fazOutraCoisa(a, b):
    x = a
    a = b
    b = x

def fazAlgumaCoisa(x1, x2):
    x3 = x1
    x1 = x2
    x2 = x3

def fazAindaMais(x1, x2):
    x3 = x1
    i = 0
    while i < len(x1):
        x1[i] = x2[i]
        i += 1
    i = 0
    while i < len(x2):
        x2[i] = x3[i]
        i += 1

def fazIsso(x1, x2):
    x3 = []
    i = 0
    while i < len(x1):
        x3.append(x1[i])
        i += 1
    i = 0
    while i < len(x1):
        x1[i] = x2[i]
        i += 1
    i = 0
    while i < len(x2):
        x2[i] = x3[i]
        i += 1
