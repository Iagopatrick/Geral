def imprime(L, i = 0):
    if i < len(L):
        if type(L[i]) == int:
            print(L[i])
            imprime(L, i + 1)
        else:
            imprime(L, i + 1)

def main():
    info = ["Pedro", 20, 1.73, "Vitoria", True, 9.5, 9, 0, 10]
    imprime(info)

main()