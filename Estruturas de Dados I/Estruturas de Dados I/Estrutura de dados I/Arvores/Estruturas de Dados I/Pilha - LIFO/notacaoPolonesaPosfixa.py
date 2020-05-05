import PilhaD
p1=PilhaD.PilhaD()

def main():
    exp = '234+*5/6-'
    print('Expressão:',exp,'\nResultado:', polonesa(exp))

def polonesa(exp):
    i=0
    while i<len(exp): 
        if exp[i].isdigit():
            p1.push(exp[i])
        else:
            if p1.quant>=2:
                resultado=''
                x2=float(p1.getTopo().info)
                p1.pop()
                x1=float(p1.getTopo().info)
                p1.pop()
                if exp[i]=='+':
                    resultado=x1+x2
                elif exp[i]=='-':
                    resultado=x1-x2
                elif exp[i]=='*':
                    resultado=x1*x2
                elif exp[i]=='/':
                    resultado=x1/x2
                p1.push(resultado)
            else:
                i=len(exp)
        i+=1
    return p1.getTopo().info

main()
