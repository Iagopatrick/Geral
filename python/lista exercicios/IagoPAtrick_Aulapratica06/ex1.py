def fatorial(n):
    if type(n) == int and n >= 0:
        if n == 1 or n == 0:
            return 1
        else:
            return n*fatorial(n-1)
    else:
        return "Erro: Digite valores válidos (positivos e inteiros)"
    
def main():
    n = 2
    print(f"{n}! = {fatorial(n)}")

    n = 2.5
    print(f"{n}! = {fatorial(n)}")
    
    n = -2
    print(f"{n}! = {fatorial(n)}")
    
main()