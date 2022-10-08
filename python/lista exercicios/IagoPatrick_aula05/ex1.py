def soma1():
    x = float(input("Digite um número: "))
    y = float(input("Digite outro: "))
    return x+y

def soma2(x, y):
    return x+y

def main():
    print(soma1())
    print(soma2(3, 4))
main()