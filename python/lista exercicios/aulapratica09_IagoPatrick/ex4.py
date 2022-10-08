import random as r 
def myRange1(n, L=[], i=0):
    if i == n:
        return L + [i]  #se inverter ele faz a lista contraria [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        return myRange1(n, L + [i], i+1)


def myRange2(A,B,li = []):
    """retorna uma lista dos números de A a B, contudo, se A > B retorna lista vazia """

    if A <= B:
        return myRange2(A + 1, B, li + [A])
    else:
        return li

def myRange3(a, b, s = 1, li = []):
    if a <= b:
        if s == 1:
            return myRange2(a,b)
        else:
            return myRange3(a + s, b, s, li + [a])

    else:
        return li


def myRange(a, b = 1, s = 1, li = []):
    
    if b == 1:
        return myRange1(a)
    elif a <= b:
        if s == 1:
            return myRange2(a,b)
        else:
            return myRange3(a, b, s)
    else:
        return li
    
def sorteioMegaSena(i = 0, li = myRange(1,60), l = []):
    
    n = r.choice(li)
    if i < 6:
        if n not in l:
            return sorteioMegaSena(i + 1, li, l + [n])
        else:
            return sorteioMegaSena(i, li, l)
    else:
        return l

def main():
    print(sorteioMegaSena())
main()