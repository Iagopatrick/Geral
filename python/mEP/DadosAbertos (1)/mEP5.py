######################################################
# Programação Funcional / Programção I (2021/2)
# miniEP5 - Jogo da Velha
# Nome: IAGO PATRICK DE MELO GRIPP VILAS BOAS 
# Matrícula: 2021200087
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do 
#   Paradigma Funcional.
# - Você não pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Você deve seguir o código base disponibilizado, 
#   não sendo permitido a alteração do nome e/ou
#   lista de parâmetros das funções dadas;
# - Caso precise, você PODE criar outras funções;
# - Não é permitido a utilização de lista, tuplas 
#   ou qualquer outro tipo estruturado para 
#   “facilitar” a manipulação dos dados. Você deve 
#   sempre trabalhar com as 9 variáveis que 
#   representam as posições no tabuleiro;
#
# Dica: Leia o docstring de cada função para saber o
#       que cada uma deve fazer e retornar.
######################################################

def verificacao(p):
    """
    Verifica se o valor da posição é válida e retorna True ou False conforme se é váilido("x", "o", " ") ou não
    """
    return True if p == " " or p == "x" or p == "o" or p == "" else False

def opcao(p):
    """
    Recebe como parametro X ou O e então retorna True para X e False para O
    """
    if p == "x":
        return True
    elif p == "o":
        return False

def soma(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """Identifica se existe um X ou O em cada posição e retorna a quantidade de cada um"""
    x = 0
    o = 0
    if opcao(p1) == True:
        x += 1
    if opcao(p1) == False:
        o += 1
    if opcao(p2) == True:
        x += 1
    if opcao(p2) == False:
        o += 1
    if opcao(p3) == True:
        x += 1
    if opcao(p3) == False:
        o += 1
    if opcao(p4) == True:
        x += 1
    if opcao(p4) == False:
        o += 1
    if opcao(p5) == True:
        x += 1
    if opcao(p5) == False:
        o += 1
    if opcao(p6) == True:
        x += 1
    if opcao(p6) == False:
        o += 1
    if opcao(p7) == True:
        x += 1
    if opcao(p7) == False:
        o += 1
    if opcao(p8) == True:
        x += 1
    if opcao(p8) == False:
        o += 1
    if opcao(p9) == True:
        x += 1
    if opcao(p9) == False:
        o += 1   
    return x, o

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    #Complete o código da função preciso usar print
    m = "-" * 3 + "+" + "-" * 3 + "+" + 3 * "-"
    print(f" {p7} | {p8} | {p9} \n{m}\n {p4} | {p5} | {p6} \n{m}\n {p1} | {p2} | {p3} ")

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    #Complete o código da função
    valido = 0
    if verificacao(p1) == True:
        valido += 1
    if verificacao(p2) == True:
        valido += 1
    if verificacao(p3) == True:
        valido += 1
    if verificacao(p4) == True:
        valido += 1
    if verificacao(p5) == True:
        valido += 1
    if verificacao(p6) == True:
        valido += 1
    if verificacao(p7) == True:
        valido += 1
    if verificacao(p8) == True:
        valido += 1
    if verificacao(p9) == True:
        valido += 1
    return True if valido == 9 else False

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    #Complete o código da função | a soma total de jogadas podem ser 9, ou seja jogadas de x + o = 9, sendo o primeiro a jogar 
    # tendo mais jogadas que o segundo, ou seja x != o. se x repetir muitas vezes ele fica invalido
    x, y = soma(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    if x - y == 1 or y - x == 1 or x == y:
        return True
    else:
        return False
    
def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    #Complete o código da função
    x, y = soma(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    if x + y >= 5:
        # if  x == y:
        #     print("O jogo nao terminou!")
        if p1 == p2 == p3 or p1 == p5 == p9 or p1 == p4 == p7 :
            print(f"O jogador '{p1}' venceu!")
        elif p4 == p5 == p6 or p9 == p6 == p3:
            print(f"O jogador '{p6}' venceu!")
        elif p7 == p8 == p9 or p7 == p5 == p3:
            print(f"O jogador '{p7}' venceu!")
        elif p2 == p5 == p8:
            print(f"O jogador '{p2}' venceu!")
        elif x + y != 9 or x == y:
            print("O jogo nao terminou!")
        elif x + y == 9:
            print("Empate!")
    else:
        print("O jogo nao terminou!")
    
######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
######################################################
def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()

