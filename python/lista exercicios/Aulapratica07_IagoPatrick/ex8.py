import random as r


def maiormenor(a, b, c, d, e, f):
    """Recebe 6 valores dos acertos(acertos1 até acertos6) e retorna qual é maior e qual é menor"""
    maior = "" 
    menor = ""
    if a > b and a > c and a > d and a > e and a > f:
        maior = "maior número de acertos foram: 1"
    elif b > a and b > c and b > d and b > e and b > f:
        maior = "maior número de acertos foram: 2"
    elif c > a and c > b and c > d and c > e and c > f:
        maior = "maior número de acertos foram: 3"
    elif d > a and d > c and d > b and d > e and d > f:
        maior = "maior número de acertos foram: 4"
    elif e > a and e > c and e > d and e > b and e > f:
        maior = "maior número de acertos foram: 5"
    elif f > a and f > c and f > d and f > e and f > b:
        maior = "maior número de acertos foram: 6"
    else:
        maior = "Não teve maior número de acertos"

    if a < b and a < c and a < d and a < e and a < f:
        menor = "menor número de acertos foi: 1"
    elif b < a and b < c and b < d and b < e and b < f:
        menor = "menor número de acertos foi: 2"
    elif c < a and c < b and c < d and c < e and c < f:
        menor = "menor número de acertos foi: 3"
    elif d < a and d < c and d < b and d < e and d < f:
        menor = "menor número de acertos foi: 4"
    elif e < a and e < c and e < d and e < b and e < f:
        menor = "menor número de acertos foi: 5"
    elif f < a and f < c and f < d and f < e and f < b:
        menor = "menor número de acertos foi: 6"
    else:
        menor = "Não teve menor número de acertos"
    return maior, menor


def igual(n, a, b, c, d, e, f):
    """Recebe um valor n retorna se ele é igual a outros 6 números apostados e retorna True ou False"""
    return True if n == a or n == b or n == c or n == d or n == e or n == f else False

def soma(n, a, b, c, d, e, f):
    """Recebe um valor n e outros 6 números apostados e, com a função igual, retorna 1 se igual for True e 0 se for False"""
    igual(n, a, b, c, d, e, f)
    if igual == True:
        return 1
    else:
        return 0

def megaSena(a, b, c, d, e, f):
    """Recebe 6 valores apostados pelo jogador e retorna quantos ele acertou"""
    i = r.randint(1, 60)
    j = r.randint(1, 60)
    k = r.randint(1, 60)
    l = r.randint(1, 60)
    m = r.randint(1, 60)
    n = r.randint(1, 60)
    soma1 = soma(i, a, b, c, d, e, f) + soma(j, a, b, c, d, e, f) + soma(k, a, b, c, d, e, f)
    soma2 = soma(l, a, b, c, d, e, f) + soma(m, a, b, c, d, e, f) + soma(n, a, b, c, d, e, f)
    return soma1 + soma2

def desafio(a, b, c, d, e, f, z, y = 0, acertos1 = 0, acertos2 = 0, acertos3 = 0, acertos4 = 0, acertos5 = 0, acertos6 = 0, acertos = 0):
    """Recebe os valores apostados (de 'a' até 'f') e o número de tentativas z. Retorna a média de acertos, o menor número de acertos e o maior número de acertos"""
    if y == z:
        Maior, Menor = maiormenor(acertos1, acertos2, acertos3, acertos4, acertos5, acertos6)
        return Menor, Maior, acertos / z
    else:
        x = megaSena(a, b, c, d, e, f)
        if x == 6:
            return desafio(a, b, c, d, e, f, z, y + 1, acertos1, acertos2, acertos3, acertos4, acertos5, acertos6 + 1, acertos + 1)
        elif x == 5:
            return desafio(a, b, c, d, e, f, z, y + 1, acertos1, acertos2, acertos3, acertos4, acertos5 + 1, acertos6, acertos + 1)
        elif x == 4:
            return desafio(a, b, c, d, e, f, z, y + 1, acertos1, acertos2, acertos3, acertos4 + 1, acertos5, acertos6, acertos + 1)
        elif x == 3:
            return desafio(a, b, c, d, e, f, z, y + 1, acertos1, acertos2, acertos3 + 1, acertos4, acertos5, acertos6, acertos + 1)
        elif x == 2:
            return desafio(a, b, c, d, e, f, z, y + 1, acertos1, acertos2 + 1, acertos3, acertos4, acertos5, acertos6, acertos + 1)
        elif x == 1:
            return desafio(a, b, c, d, e, f, z, y + 1, acertos1 + 1, acertos2, acertos3, acertos4, acertos5, acertos6, acertos + 1)
        elif x == 0:
            return desafio(a, b, c, d, e, f, z, y + 1, acertos1, acertos2, acertos3, acertos4, acertos5, acertos6, acertos)


def main():
    a = input("Digite sua primeira aposta ")
    b = input("Digite sua segunda aposta ")
    c = input("Digite sua terceira aposta ")
    d = input("Digite sua quarta aposta ")
    e = input("Digite sua quinta aposta ")
    f = input("Digite sua sexta aposta ")
    maior, menor, media = desafio(a, b, c, d, e, f, 80)
    print(megaSena(a, b, c, d, e, f))
    print(f"O maior número de acertos em 80 tentativas foi: {maior}")
    print(f"O menor número de acertos em 80 tentativas foi: {menor}")
    print(f"A média de acertos foi: {media}")
main()