def f1(n, i=0, soma=0):
   if i <= n:
       return f1(n, i+1, soma+i)
   else:
       return soma

def imprimeSoma(x, y = 1):
    #  caso base: x = y
    if x == y:
        print(f"{x} = {f1(x)}")
    else:
        print(f"{y} = {f1(y)}")
        imprimeSoma(x, y + 1)
        


def main():
    
    imprimeSoma(5)
    imprimeSoma(2)

main()
