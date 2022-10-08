def desenha1(n, c = "*", i = 1):
    """coloca a quantidade (n) de str (c) em quantas linhas (i) o usuario deseja"""
    if i <= n:
        print(c*n)
        desenha1(n, c, i + 1)

def desenha2(n, c = "*", i = 1):
    """
    coloca a quantidade (n) de str (c) em quantas linhas (i) o usuario deseja, fazendo em ordem crescente
    """
    if i <= n:
        print(c*i)
        desenha2(n, c, i + 1)

def desenha3(n, c = "*", i = 1):
    """
    coloca a quantidade (n) de str (c) em quantas linhas (i) o usuario deseja, fazendo em ordem como se "empilhados"
    ex:  *
        ***
       *****
    """
    if n % 2 == 1:
        print("n deve ser impar")
    elif i <= n:
        ne = (n-i)//2
        print(" "*ne + c*i)
        desenha3(n, c, i + 2)


def main():
    desenha1(5,"-",2)
    desenha1(4, "vivo")
    desenha2(5)
    desenha2(6, "roma", 2)
    desenha3(3)
    desenha3(6)
    desenha3(6, "v", 3)

main()

