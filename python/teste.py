# #backup 15/03 16:55

# #tenho que fazer uma função que consiga ler se os valores de uma lista são iguais ao indice de outra e contabilizar
# #exemplo: uma lista com os votos[1,1,1,1,1,1,2,3,] eu preciso contar esses votos de forma que eu conte quantos 1 tem ai, quantos 2 e quantos 3
# def NomeCandidatos(n, lista, i = 0,):
#     """Recebe o nome dos candidatos. Retorna a lista contento esses nomes"""
#     if i < n:
#         x = input()
#         lista[i] = x
#         return NomeCandidatos(n, lista, i + 1)
#     else:
#         # print (lista)
#         return lista
# def votantes(n, lista, i = 1):
#     """Recebe o voto de cada participante. Retorna a lista desses votos"""
#     if i < len(lista):
#         x = int(input())
#         lista[i] = x
#         return votantes(n, lista, i + 1)
#     return lista

# def contagem(l, l2, i = 0, l1 = []):
#     """
#     receber a lista de votos (l), lista da quantidade de votos (l2). Retorna a lista com os votos em seus respectivos indices
#     """
#     if len(l) > i:
#         l1 += [soma(l, i)]
#         return contagem(l, l2, i + 1, l1)
#     else:
#         return l1

    


# def soma(lista, x, i = 1, j = 0):
#     """
#     Recebe uma lista com votos e o indice o qual queremos (x) que representa o candidato. 
#     Retorna a quantidade desses votos
#     """
#     if len(lista) > i:
#         if lista[i] == x:
#             print(f"Aqui jaz a lista da soma: {lista}")
#             return soma(lista, x, i + 1, j + 1)
#         else:
#             return soma(lista, x, i + 1, j)
#     else:
#         print(f"aqui jaz j {j}")
#         return j



# def urna():
#     nCandidates = int(input())
    
#     z = list(range(nCandidates + 1))

#     cadidates = NomeCandidatos(nCandidates, z)
    
#     nVotos = int(input())
    
#     x = list(range(nVotos + 1))
    
#     votos = votantes(nVotos, x)
#     print(f"votos {votos}")
#     y = contagem(votos, z)
    
#     print(y)




# def main():
#     """"""
#     urna()

# main()

# backup 15/03 21:06
#o ultimo print ainda ta errado


def NomeCandidatos(n, lista, i = 1,):
    """Recebe o nome dos candidatos. Retorna a lista contento esses nomes"""
    if i < len(lista) - 1:
        x = input()
        lista[i] = x
        return NomeCandidatos(n, lista, i + 1)
    else:
        # print (lista)
        return lista
def votantes(x, lista, i = 1):
    """Recebe o voto de cada participante. Retorna a lista desses votos"""
    if i < len(lista):
        n = int(input())
        lista[i] = n
        return votantes(x, lista, i + 1)
    return lista

def contagem(l, l2, i = 0, l1 = []):
    """
    receber a lista de votos (l), lista da quantidade de votos (l2). Retorna a lista com os votos em seus respectivos indices
    """
    if len(l) > i:
        l1 += [soma(l, i)]
        return contagem(l, l2, i + 1, l1)
    else:
        return l1

def imprime(l1, l2, i = 1):
    """Recebe a lista dos candidatos (l1) e a lista da quantidade dos votos (l2). Junta as informações e faz a impressão deles"""
    if len(l1) > i:
            print(f"{l1[i]} : {f'{l2[i]} voto' if l2[i]<= 1 else f'{l2[i]} votos' }")
            return imprime(l1, l2, i + 1)

    print(f"Brancos: {l2[0]}")
    print(f"Nulos: {f'{l2[i]} voto' if l2[i]<= 1 else f'{l2[i]} votos' }")
def soma(lista, x, i = 1, j = 0):
    """
    Recebe uma lista com votos e o indice o qual queremos (x) que representa o candidato. 
    Retorna a quantidade desses votos
    """
    if len(lista) > i:
        if lista[i] == x:
            # print(f"Aqui jaz a lista da soma: {lista}")
            return soma(lista, x, i + 1, j + 1)
        else:
            return soma(lista, x, i + 1, j)
    else:
        # print(f"aqui jaz j {j}")
        return j



def urna():
    nCandidates = int(input())
    z = list(range(nCandidates + 2))
    candidates = NomeCandidatos(nCandidates, z)
    

    nVotos = int(input("a "))
    x = list(range(nVotos + 1))
    votos = votantes(nVotos, x)
    
    
    
    print(x)
    print(f"votos {votos}")
    y = contagem(votos, z)
    # print(candidates)
    # print(y)
    imprime(candidates, y)



def main():
    """"""
    urna()

main()