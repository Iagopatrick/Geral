x = float(input("Digite um valor:"))
op = input("Digite a operação: ")
y = float(input("Digite outro valor: "))
# se op == "+" -> imprimir x + y
# se op == "-" -> imprimir x - y
if op == "+":
    print(f"{x} {op} {y} = {x+y}")
else:
    if op =="-":
        print(f"{x} {op} {y} = {x - y}")
    else:
        if op == "*":
             print(f"{x} {op} {y} = {x * y}")
        else:
             print("operaçã invalida")


# menos eficiente
# if op == "+":
#     print(f"{x} {op} {y} = {x + y}")
# if op == "-":
#     print(f"{x} {op} {y} = {x - y}")
# if op == "*":
#     print(f"{x} {op} {y} = {x * y}")
# if not (op == "+" or op == "-" or op == "*"):
#     print("Operação invalida")    
