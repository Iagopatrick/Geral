x = int(input("Digite um número: "))
if x%2 == 0:
    print(f"{x} é par")
elif x%2 == 1:
    print(f"{x} é impar")
if x%2 == 0 and x%3 == 0:
    print(f"{x} é divisível por 2 e por 3")
if x%2 == 0 and x%5 == 0:
     print(f"{x} é divisível por 2 e por 5")
