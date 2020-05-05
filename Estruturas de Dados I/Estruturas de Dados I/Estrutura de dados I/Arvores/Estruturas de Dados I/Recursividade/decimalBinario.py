def decBin(n):
    if n == 0:
        return ""
    else:
        return decBin(n//2)+str(n%2)
print(decBin(234))
