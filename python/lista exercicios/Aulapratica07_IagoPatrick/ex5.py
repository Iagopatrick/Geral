def b(n):
    if type(n) != int or n < 0: #n deve ser um número natural
        print("ERRO: O argumento deve ser inteiro positivo")
        return None
    elif n < 2: #Você consegue pensar em uma forma de simplificar essa parte?
       return 0 if n == 0 else 1
       
    else: #Você consegue pensar em uma forma de simplificar o return?
         return b(n//2) * 10 + n%2

def main():
    print("b(1) =", b(1))
    print("b(2) =", b(2))
    print("b(3) =", b(3))
    print("b(4) =", b(4))
    print("b(10) =", b(10))
    print("b(21) =", b(21))
    print("b(0) =", b(0))
    print("b(9) =", b(9))
    print("b(1220) =", b(1220))
    #Faça outros testes

main()