def soma(n):
    return ((1+n)*n)/2
def main():
    x = int(input())
    y = input()
    a = y.split()
    elista = list(map(int, a))
    c = sum(elista)
    z = soma(x)
    print(int(z-c))
    

main()