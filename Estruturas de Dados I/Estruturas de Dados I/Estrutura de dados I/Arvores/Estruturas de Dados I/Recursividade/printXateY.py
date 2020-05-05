def xToY(x,y):
    if x==y:
        return x
    else:
        return str(x)+'\n'+str(xToY(x-1,y))
    
    
print(xToY(10,-100))
