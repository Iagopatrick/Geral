n = int(input("Diite um número: "))

# Par ou impar
if n % 2 == 0:
    print(f"{n} é par")
else:# if not n % 2 == 0:
    print(f"{n} é impar")

# Divisível por 3
if n % 3 == 0:
    print(f"{n} é divisível por 3")
else: # if n % 3 != 0:
    print(f"{n} não é divisivel por 3")

# Verificar se é divisivel por 2 e 3
if n % 2 == 0 and n % 3 ==0:
    print(f"{n} é divisivel por 2 e 3")

# Divisivel por 3 ou por 5
if n % 5 == 0 or n % 3 == 0:
    print(f"{n} é divisivel por 3 ou 5")

# Verificar se n é 1 or 3 ou 10
if n == 1 or n == 3 or n == 10:
    print("Ok")   
