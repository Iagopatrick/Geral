import math as m
def combinacoes(n, p):
    x = m.comb(n, p)
    print(f"{x}")

def main():
    n = int(input("Digite o números de elementos: "))
    p = int(input("Digite a quantidade de elementos por grupo: "))
    combinacoes(n, p)

main()