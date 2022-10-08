def semRepetidos(li, li2 = [], i = 0):
    if len(li) > i:
        if li[i] not in li2:
            return semRepetidos(li, li2 + [li[i]], i + 1)
        else:
            return semRepetidos(li, li2, i + 1)
    else:
        return li2

def main():
    print(semRepetidos([1, 2, 1, 3, 2, 1, 4, 0]))
    print(semRepetidos([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
main()