def P(n):
    """Identifica se o número é primo ou não e retorna True se for primo"""
    if n == 2 or n == 3 or n == 5:
        return True
    if n%2 == 0 or n % 3 == 0 or n % 5 == 0 or n == 1:
        return False
    else:
        return True

def main():
    print("1 = ", P(1))
    print("2 = ", P(2))
    print("3 = ", P(3))
    print("4 = ", P(4))
    print("5 = ", P(5))
    print("6 = ", P(6))
    print("7 = ", P(7))
    print("8 = ", P(8))
    print("9 = ", P(9))
    print("10 = ", P(10))
    print("11 = ", P(11))
    print("12 = ", P(12))
    print("13 = ", P(13))
    print("17 = ", P(17))
    print("127 = ", P(127))
    #Faça outros testes


main()