def votantes(lr, nv, i = 1):
    """
    Parametros: Lista n(numero de votos) espaços com [0], numero de votos, numero de candidatos
    Ele faz a leitura do voto e coloca em uma lista
    Retorna uma lista que contenha a quantidade de votos de cada candidato
    """
    if nv >= i:
        v = int(input())
        if v == 0:
            lr[i] += 1
        elif v > nv:
            lr[nv + 1] += 1
        else:
            lr[i] += 1
        return votantes(lr, nv, i + 1)
    else:
        print(lr)
        return lr

def candidatos(lr, i = 1):
    """
    Parametro: Lista range de 0 a n (numeros de candidatos)
    Faz a leitura dos nomes dos candidatos e os coloca em uma lista
    Retorna uma lista com os nomes dos candidatos em seus respectivos indices
    """
    if len(lr) - 1 > i: #-1 tira os nulos
        c = input()
        lr[i] = c
        return candidatos(lr, i + 1)
    print(lr)
    return lr

def vencedor(lc, lv, i = 1, j = 0, k = 0): # a variavel j guarda o elemento e o k guarda o indice
    """
    Parametros: lista dos candidatos, lista dos votos
    Olha qual é o maior, tirando os brancos e os nulos
    """
    if len(lv) - 1> i:
        if lv[i] > j:
            return vencedor(lc, lv, i + 1, lv[i], i)
        else:
            return vencedor(lc, lv, i + 1, j, k)
    return lc[k]

def imprime(lc, lv, i = 1): #i = 1 porque não preciso que ele percorra nos nulos
    """
    Parametros: Lista com os nomes dos candidatos, Lista dos votos
    Faz a impressão dos candidatos com seus respectivos votos candidato: voto e de quem venceu
    """
    if len(lc) - 1> i: #tem o -1 pois ele não conta os nulos também
        print(f"{lc[i]}: {lv[i]}")
        return imprime(lc, lv, i + 1)
    else:
        print(f"Brancos: {lv[0]}")
        if len(lc) > len(lv):
            print(f"Nulos: 0")
        else:
            print(f"Nulos: {lv[i]}")
        print(f"Vencedor(a): {vencedor(lc, lv)}")


def main():
    c = int(input())
    listac = [0] * (c + 2) # + 1 vai até o numero de candidatos e +2 adiciona os nulos
    cd = candidatos(listac[:]) #usa o [:] para não fazer com que a lista range muda (uso da mesma memória)

    v = int(input())
    # if v >= c:
    #     listav = [0] * (v + 2)
    # else:
    listav = [0] * (c + 2)
    vt = votantes(listav[:], v)

    imprime(cd, vt)

main()