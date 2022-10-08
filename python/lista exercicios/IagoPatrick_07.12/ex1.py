import math as m

x = float(input("Digite o valor de x: "))

if x <= 1:
    print(f"Esse é o valor de fx: {m.log(abs(x))}")
elif 1 < x <= 2:
    print(f"Esse é o valor de fx: {m.log(x, 10) + m.sqrt(x)}")
elif 2 < x <= 5:
    print(f"Esse é o valor de fx: {x**2 + m.exp(x)}")
elif x > 5:
    print(f"Esse é o valor de fx: {x**(x/2) + m.log2(x)}")


