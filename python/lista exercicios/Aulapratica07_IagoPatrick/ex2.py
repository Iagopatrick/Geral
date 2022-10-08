def f1(n, x = 0):
    """Retorna a quantidade de números naturais pares menores ou iguais a n"""
    if n == 0:
        return x 
    elif n % 2 == 0:
        return f1(n - 2, x + 1) #Por que n - 2? um numero par -2 continua sendo par até chegar em 0
    elif n % 2 != 0:
        return f1(n - 1) #Por que n - 1? por um numero impar -1 se torna par e entra na outra linha do codigo
def f2(n):
    """Retorna a soma dos números naturais menores ou iguais a n"""
    return 1 if n == 1 else n + f2(n - 1)

def main():
     print(f1(10))
     print(f2(5)) 
main()