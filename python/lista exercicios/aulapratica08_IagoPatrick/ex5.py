def todosNumeros(L, i = 0):
    if len(L) > i:
        if type(L[i]) != int and type(L[i]) != float:
            return False
        else:
            return todosNumeros(L, i + 1)
    else:
        return True
def main():
    l1 = [1, 2, 3]
    l2 = [1.5, -3.8, -4.5, 6.2]
    l3 = ["UFES", 1, 3.7, 2.5]
    l4 = [True, False, True]
    if todosNumeros(l1) == True:
        print(f"l1 contém apenas números")
    else:
        print("Não contém somente números")

    if todosNumeros(l2) == True:
        print(f"l2 contém apenas números")
    else:
        print("Não contém somente números")

    if todosNumeros(l3) == True:
        print(f"l3 contém apenas números")
    else:
        print("Não contém somente números")

    if todosNumeros(l4) == True:
        print(f"l4 contém apenas números")
    else:
        print("Não contém somente números")
main()