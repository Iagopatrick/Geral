n = int(input("Digite um número: "))
x = int(n//100)
y = int((n/10)%10)
z = int(n%10)
if n>999 or n<100:
    print("ERRO - Apenas valores entre 100 e 999 são aceitáveis")
elif x < y < z:
    print(f"{x} {y} {z}")
    print(f"{n} é ascendente")
else:
    print(f"{n} não é ascendente")