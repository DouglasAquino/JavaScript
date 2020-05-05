
def bin(x):
    if x==1 or x==0:
        return str(x)
    else:
        return bin(x//2)+str(x%2)
    
print(bin(16))

def bin(16):
    if x==1 or x==0:
        return str(x)
    else:
        return bin(8)+str(0)
    

def bin(8):
    if x==1 or x==0:
        return str(x)
    else:
        return bin(4)+str(0)


def bin(4):
    if x==1 or x==0:
        return str(x)
    else:
        return bin(2)+str(0)

def bin(2):
    if x==1 or x==0:
        return str(x)
    else:
        return bin(1)+str(0)

def bin(1):
    if x==1 or x==0:
        return str(1)
    else:
        return bin(x//2)+str(x%2)
'''    
