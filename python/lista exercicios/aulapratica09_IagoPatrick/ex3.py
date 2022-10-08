def uniao(l1, l2, li = [], i= 0, j = 0):
    if len(l1) > i:
        if l1[i] not in li:
            return uniao(l1, l2, li + [l1[i]], i + 1, j)
        else:
            return uniao(l1, l2, li, i + 1)
    elif len(l2) > j:
        if l2[j] not in li:
            return uniao(l1, l2, li + [l2[j]], i, j + 1)
        else:
            return uniao(l1, l2, li, i, j + 1)
    else:
        return li


def concatena(L, i = 0, s = ""):
    """
    Faz a concatenação dos elementos da lista
    
    """

    if i < len(L):
        return concatena(L, i + 1, s + L[i])
    else:    
        return s

def fim(lista):
    """
    verifica se alguém venceu o jogo e retorna quem venceu (se houver empate retorna "Empate" e se o jogo ainda nao acabou ele  retorna "jogo nao acabou").
    """
    # v = ""
    # n, m = quantidade(lista)

    if concatena(lista[1:4]) == "XXX" or concatena(lista[1:4]) == "OOO":
        return lista[1]
    elif concatena(lista[4:7]) == "XXX" or concatena(lista[4:7]) == "OOO":
        return lista[4]
    elif concatena(lista[7:10]) == "XXX" or concatena(lista[7:10]) == "OOO":
        return lista[7]
    elif concatena(lista[1:9:3]) == "XXX" or concatena(lista[1:9:3]) == "OOO":
        return lista[1]
    elif concatena(lista[2:9:3]) == "XXX" or concatena(lista[2:9:3]) == "OOO":
        return lista[2]
    elif concatena(lista[3:9:3]) == "XXX" or concatena(lista[3:9:3]) == "OOO":
        return lista[3]
    elif concatena(lista[1:10:4]) == "XXX" or concatena(lista[1:10:4]) == "OOO":
        return lista[1]
    elif concatena(lista[3:8:2]) == "XXX" or concatena(lista[3:8:2]) == "OOO":
        return lista[3]
    # elif " " in lista:
    #     return "Jogo nao acabou"
    # else:
    #     return "Empate"
    


def main():
    print(uniao([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,5,5,5,2,2,20]))
    print(uniao([1,2], [10,20,1,2]))
    print(uniao([" ","x"," ","x"], ["o", "x"]))
    lista = [" ", "X","X","X"]
    # print(lista[3])
    print(concatena(lista[1:4]))
    print(fim(lista))
main()