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
    


# L = myRange1(10)
# print(L) #Saida esperada: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(myRange2(10,20)) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(myRange2(10,5)) #[]
# print()
# print(myRange3(10,20, 2)) # [10, 12, 14, 16, 18]
# print(myRange3(1,18, 3)) # [1, 4, 7, 10, 13, 16]
# print(myRange3(10,20)) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


def main():
    print(myRange(10)) #Saida esperada: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(myRange(2, 10)) #Saida esperada: [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(myRange(10, 2)) #Saida esperada: []
    print(myRange(0, 10, 2)) #Saida esperada: [0, 2, 4, 6, 8, 10]
    print(myRange(5, 30, 5)) #Saida esperada: [5, 10, 15, 20, 25, 30]
main()
