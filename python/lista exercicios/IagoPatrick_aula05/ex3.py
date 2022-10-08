import math as m
def areaEsfera1():
    r = float(input("Digite o valor do raio: "))
    area = 4 * m.pi * r**2
    print(area)
def areaEsfera2(r):
    a = 4 * m.pi * r**2
    print(a)
def areaEsfera3(r):
    a = 4 * m.pi * r**2
    return a
def main():
    areaEsfera1(3)
    areaEsfera2()
    print(areaEsfera3())

main()