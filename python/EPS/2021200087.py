######################################################
# Programação Funcional / Programção I (2021/2)
# EP2 - Jogo da Velha
# Nome: Iago Patrick de Melo Gripp Vilas Boas
# Matrícula: 2021200087
######################################################


#anotações de erro:
# conferir se as vitorias estão sendo computadas certas



import random as r 
from os import system, name
from tokenize import tabsize
from xml.etree.ElementTree import TreeBuilder 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2021200087" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Iago Patrick de Melo Gripp Vilas Boas" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def validade(msg, msgerro, tipo):
    try:
        x = tipo(input(msg))
        if type(x) == int:
            if 1<= x <= 9:
                return x
            else:
                print(msgerro)
                return validade(msg, msgerro, tipo)
        elif type(x) == str:
            if x == "o" or x == "O":
                return "O"
            elif x == "X" or x == "x":
                return "X"
            else:
                print(msgerro)
                return validade(msg, msgerro, tipo)
    except:
        print(msgerro)
        return validade(msg, msgerro, tipo)

def ptabuleiro(lista):
    """Printa o tabuleiro da tela, recebendo a lista das casas como parâmetro"""
    print(f" {lista[7]} | {lista[8]} | {lista[9]} ")
    print("---+---+---")
    print(f" {lista[4]} | {lista[5]} | {lista[6]} ")
    print("---+---+---")
    print(f" {lista[1]} | {lista[2]} | {lista[3]} ")

def quantidade(lista, i = 0, v = 0):#i = variante para percorrer a lista toda/ x = números de X/ o = números de O
    """
    Recebe uma lista como parametro. Analisa cada elemento da lista e retorna a quantidade de espaços vazios
    """
    if i < 10:
        if lista[i] == " ":
            return quantidade(lista, i + 1, v + 1)
        else:
            return quantidade(lista, i + 1, v )
    return v
    
def concatena(L, i = 0, s = ""):
    """
    Faz a concatenação dos elementos da lista
    
    """

    if i < len(L):
        return concatena(L, i + 1, s + L[i])
    else:    
        return s

def jogada(lista):
    """Faz a jogada do jogador, usada para evitar erros ao colocar o numero de uma casa invalida"""
    n = validade("Escolha a casa na qual você irá jogar (1-9): ", "Digite valores válidos! (1-9)", int)
    if lista[n] == " ":
        return n
    else:
        print("Jogada inválida! Selecione uma casa disponível!")
        return jogada(lista)

def fim(lista):
    """
    verifica se alguém venceu o jogo e retorna quem venceu (se houver empate retorna "Empate" e se o jogo ainda nao acabou ele  retorna "jogo nao acabou").
    """
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
    elif concatena(lista[3:10:3]) == "XXX" or concatena(lista[3:9:3]) == "OOO":
        return lista[3]
    elif concatena(lista[1:10:4]) == "XXX" or concatena(lista[1:10:4]) == "OOO":
        return lista[1]
    elif concatena(lista[3:8:2]) == "XXX" or concatena(lista[3:8:2]) == "OOO":
        return lista[3]
    elif " " in lista[1:10]:
        return "Jogo nao acabou"
    else:
        return "Empate"
    
def first():
    """Define quem joga primeiro: 1 jogador, 2 Pc"""
    n = r.choice([1,2])
    return n

def lastplay(lista, i = 1 ): #i = 1 para ele não jogar na posição 0, que é uma posição inválida
    """Confere qual o ultimo espaço disponivel da lista e retorna o indice"""
    if i < len(lista):
        if lista[i] == " ":
            return i
        else:
            return lastplay(lista, i +1)
    
def tabuleiro(simbolo, casa, li):
    """
    Recebe o símbolo e a casa que o jogador ou o computador escolher como parametro e retorna uma lista com os valores
    
    """
    # jogada = validade("Escolha a casa na qual você irá jogar (1-9): ", int)
    #Colocar as jogadas do computador e usuario aqui dentro, de forma que tudo seja conferido aqui e na main so execute
    #Ou fazer outra função que seria o "Jogo" que vai juntar todas as funções criadas e vai executar, mas pode ser feito no próprio main
    #adicionar o simbolo a casa
    # if li[jogada] == " ":
    li[casa] = simbolo
    return li

def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador
    i: vai contar em qual jogada ele esta, ajuda na estrategia

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Explique aqui, de forma resumida, a sua estratégia usada para o computador vencer o jogador

    ele vai jogar pelos cantos, de forma que ele vai tentar preencher 3 cantos para entao jogar no meio
    ele vai conferir o meio, se estiver preenchido, ele vai jogar nas diagonais.
    Se ele conseguir completar os cantos, sem deixar o adversario ganhar, a vitória é garantida.
    Ele sempre confere as possibilidades de vitoria do adversario, mas priorizando as suas chances de vitoria. Caso ele não consiga achar uma jogada
    pré-definida, ele então parte para aleatoriedade.

    """
    #é possivel fazer duas maneiras para ele jogar. 1° poderia ser se ele começar, ele sempre tentar jogar pelos cantos e se ele não começar, priorizar o meio
    # ou tentar jogar em cima do erro do advérsario
    #2° é possível fazer com que ele tenha 2 estilos de jogos com aleatoriedade exemplo x = r.choice(1,2) if x == 1: joga assim else: joga assim 2
    
    
    if simboloComputador == "X":
        simboloJ = "O"
    else:
        simboloJ = "X"
    n = None #Definindo essa flag, é possivel ele fazer uma jogada válida mesmo sem entrar em algum if ou elif.
    v = quantidade(tabuleiro) #impar == Jogador // Par == Pc
    
    
    #<----------- primeira rodada ------------>
    if v == 10: #quando o pc joga primeiro
        n = 1
    elif v == 9: #quando ele nao jogar primeiro, ele vai conferir se o adversario jogou em algum dos cantos, se isso acontecer, ele joga no meio
        if tabuleiro[1] == simboloJ or tabuleiro[3] == simboloJ or tabuleiro[7] == simboloJ or tabuleiro[9] == simboloJ:
            n = 5 #vai atras do empate, ou vitoria caso o jogador vacile
        else: 
            n = 1
    #<----------- segunda rodada ------------>
    elif v == 8: #Pc joga primeiro 
        if tabuleiro[1] == simboloComputador and tabuleiro[5] == simboloJ and tabuleiro[9] == " ":
            n = 9          
        elif tabuleiro[7] == simboloJ and tabuleiro[3] == " ":
            n = 3 
        elif tabuleiro[9] == simboloJ and tabuleiro[7] == " ":
            n = 7
        elif tabuleiro[3] == simboloJ and tabuleiro[9] == " ": #conferindo as outras diagonais
            n = 9
        elif tabuleiro[4] == simboloJ or tabuleiro[2] == simboloJ or tabuleiro[6] == simboloJ or tabuleiro[8] == simboloJ:
            n = 3
        elif tabuleiro[5] == simboloJ and tabuleiro[7] == " ":
            n = 7
        elif tabuleiro[3] == " ":
            n = 3
        else:
            n = 8
    elif v == 7: #Jogador joga primeiro
        if tabuleiro[5] == simboloComputador: #é preciso jogar defensivamente, pois o jogador jogou em algum dos cantos de inicio
            if tabuleiro[1] == simboloJ and tabuleiro[7] == simboloJ:
                n = 4
            elif tabuleiro[1] == simboloJ and tabuleiro[3] == simboloJ:
                n = 2 
            elif (tabuleiro[7] == simboloJ and tabuleiro[4] == simboloJ) or (tabuleiro[2] == simboloJ and tabuleiro[3] == simboloJ):
                n = 1
            elif tabuleiro[3] == simboloJ and tabuleiro[9] == simboloJ:
                n = 6
            elif (tabuleiro[3] == simboloJ and tabuleiro[6] == simboloJ) or (tabuleiro[7] == simboloJ and tabuleiro[8] == simboloJ):
                n = 9 
            elif tabuleiro[9] == simboloJ and tabuleiro[7] == simboloJ:
                n = 8
            elif (tabuleiro[1] == simboloJ and tabuleiro[4] == simboloJ) or (tabuleiro[8] == simboloJ and tabuleiro[9] == simboloJ):
                n = 7 
            elif (tabuleiro[1] == simboloJ and tabuleiro[2] == simboloJ) or (tabuleiro[9] == simboloJ and tabuleiro[6] == simboloJ):
                n = 3
            elif tabuleiro[6] == tabuleiro[1] == simboloJ and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[1] == tabuleiro[9] == simboloJ and tabuleiro[8] == " ":
                n = 8
            elif tabuleiro[3] == simboloJ == tabuleiro[7] and tabuleiro[8] == " ":
                n = 8 
            elif tabuleiro[9] == tabuleiro[2] == simboloJ and tabuleiro[3] == " ":
                n = 3
        elif tabuleiro[5] == simboloJ: 
            if tabuleiro[7] == simboloJ or tabuleiro[1] == simboloJ or tabuleiro[3] == simboloJ or tabuleiro[9] == simboloJ: #conferir se o jogador jogou nas diagonais ou centros
                if tabuleiro[1] == simboloComputador:
                    if tabuleiro[7] == simboloJ or tabuleiro[9] == simboloJ:
                        n = 3
                    elif tabuleiro[3] == simboloJ:
                        n = 7
                elif tabuleiro[3] == simboloComputador:
                    if tabuleiro[7] == simboloJ or tabuleiro[9] == simboloJ:
                        n = 1
                    elif tabuleiro[1] == simboloJ:
                        n = 9
                elif tabuleiro[9] == simboloComputador:
                    if (tabuleiro[1] == simboloJ or tabuleiro[3] == simboloJ) and tabuleiro[7] == " ":
                        n = 7 
                    elif tabuleiro[7] == simboloJ and tabuleiro[3] == " ":
                        n = 3
                elif tabuleiro[7] == simboloComputador:
                    if (tabuleiro[1] == simboloJ or tabuleiro[3] == simboloJ) and tabuleiro[9] == " ":
                        n = 9 
                    elif tabuleiro[9] == simboloJ and tabuleiro[1] == " ":
                        n = 1
            elif tabuleiro[2] == simboloJ or tabuleiro[4] == simboloJ or tabuleiro[8] == simboloJ or tabuleiro[6] == simboloJ:
                if tabuleiro[4] == simboloJ and tabuleiro[6] == " ":
                    n = 6
                elif tabuleiro[2] == simboloJ and tabuleiro[8] == " ":
                    n = 8
                elif tabuleiro[6] == simboloJ and tabuleiro[4] == " ":
                    n = 4
                elif tabuleiro[8] == simboloJ and tabuleiro[2] == " ":
                    n = 2
                elif tabuleiro[9] == simboloJ and tabuleiro[4] == " ":
                    n = 4
                elif tabuleiro[7] == simboloJ and tabuleiro[6] == " ":
                    n = 6
                elif tabuleiro[3] == simboloJ and tabuleiro[4] == " ":
                    n = 4
                elif tabuleiro[1] == simboloJ and tabuleiro[6] == " ":
                    n = 6 
        else:
            if tabuleiro[4] == tabuleiro[8] == simboloJ and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[2] == tabuleiro[6] == simboloJ and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[8] == tabuleiro[9] == simboloJ and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[9] == tabuleiro[6] == simboloJ and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[3] == tabuleiro[6] == simboloJ and tabuleiro[9] == " ":
                n = 9
            elif tabuleiro[2] == tabuleiro[5] == simboloJ and tabuleiro[8] == " ":
                n = 8
            elif tabuleiro[1] == tabuleiro[4] == simboloJ and tabuleiro[7] == " ":
                n = 7
            elif (tabuleiro[7] == tabuleiro[8] == simboloJ or tabuleiro[6] == tabuleiro[3]== simboloJ) and tabuleiro[9] == " ":
                n = 9
            elif (tabuleiro[7] == tabuleiro[4] == simboloJ or tabuleiro[2] == tabuleiro[3]== simboloJ) and tabuleiro[1] == " ":
                n = 1
            elif (tabuleiro[8] == tabuleiro[9] == simboloJ or tabuleiro[4] == tabuleiro[1]== simboloJ) and tabuleiro[7] == " ":
                n = 7
            elif (tabuleiro[1] == tabuleiro[2] == simboloJ or tabuleiro[6] == tabuleiro[9]== simboloJ) and tabuleiro[3] == " ":
                n = 3 
    #<----------- terceira rodada rodada ------------>
    elif v == 6: #Pc primeiro
        #ataque
        if tabuleiro[1] == tabuleiro[3] == simboloComputador and tabuleiro[2] == " ":
            n = 2
        elif tabuleiro[1] == tabuleiro[7] == simboloComputador and tabuleiro[7] == " ":
            n = 7
        elif tabuleiro[1] == tabuleiro[7] == simboloComputador and tabuleiro[4] == " ":
            n = 4
        elif tabuleiro[1] == tabuleiro[9] == simboloComputador and tabuleiro[5] == " ":
            n = 5
        elif tabuleiro[1] == simboloComputador == tabuleiro[3] == simboloComputador and tabuleiro[2] == simboloJ and tabuleiro[7] == " ":
            n = 7
        #defesas
        elif tabuleiro[3] == simboloJ == tabuleiro[9]:
            n = 6
        elif tabuleiro[9] ==  tabuleiro[7] == simboloJ:
            n = 8
        elif (tabuleiro[3] ==  tabuleiro[6] == simboloJ) or (tabuleiro[7] == tabuleiro[8] == simboloJ):
            n = 9
        elif (tabuleiro[9] ==  tabuleiro[8] == simboloJ) or (tabuleiro[4] == tabuleiro[1] == simboloJ):
            n = 7
        elif (tabuleiro[7] ==  tabuleiro[4] == simboloJ) or (tabuleiro[2] == tabuleiro[3] == simboloJ):
            n = 1 
        elif tabuleiro[6] == tabuleiro[9] == simboloJ:
            n = 3
        elif tabuleiro[5] == simboloJ:
            if tabuleiro[4] == simboloJ and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[8] == simboloJ and tabuleiro[2] == " ":
                n = 2
            elif tabuleiro[2] == simboloJ and tabuleiro[8] == " ":
                n = 8
            elif tabuleiro[6] == simboloJ and tabuleiro[4] == " ":
                n = 4
            elif tabuleiro[3] == simboloJ and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[9] == simboloJ and tabuleiro[1] == " ":
                n = 1 
            elif tabuleiro[9] == simboloJ and tabuleiro[1] == " ":
                n = 1
            elif tabuleiro[7] == simboloJ and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[9] == " ":
                n = 9
        elif tabuleiro[9] == tabuleiro[2] == simboloJ and tabuleiro[7] == " ":
                n = 7
        elif tabuleiro[1] == tabuleiro[3] == simboloComputador and tabuleiro[9] == " ":
            n = 9
        elif tabuleiro[1] == tabuleiro[7] == simboloComputador and tabuleiro[3] == " ":
            n = 3
        
        elif tabuleiro[5] == " ":
            n = 5           
    elif v == 5: #Jogador joga primeiro
        if tabuleiro[5] == simboloComputador:

            if tabuleiro[7] == simboloComputador and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[9] == simboloComputador and tabuleiro[1] == " ":
                n = 1
            elif tabuleiro[3] == simboloComputador and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[1] == simboloComputador and tabuleiro[9] == " ":
                n = 9
            elif tabuleiro[2] == simboloComputador and tabuleiro[8] == " ":
                n = 8
            elif tabuleiro[4] == simboloComputador and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[6] == simboloComputador and tabuleiro[4] == " ":
                n = 4
            elif tabuleiro[8] == simboloComputador and tabuleiro[2] == " ":
                n = 2
            elif tabuleiro[8] == simboloJ == tabuleiro[9] and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[8] == simboloJ and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[6] == simboloJ and tabuleiro[2] == " ":
                n = 2
            elif tabuleiro[9] == simboloJ and tabuleiro[1] != " " and tabuleiro[8] == " ":
                n = 8
            elif tabuleiro[3] == tabuleiro[2] == simboloJ and tabuleiro[1] == " ":
                n = 1 
            elif tabuleiro[4] == simboloJ and tabuleiro[2] == " ":
                n = 2
            elif tabuleiro[1] == tabuleiro[2] == simboloJ and tabuleiro[3] == " ":
                n = 3
            else: 
                
                n = lastplay(tabuleiro)
        if tabuleiro[1] == simboloComputador and tabuleiro[3] == simboloComputador and tabuleiro[2] == " ":
                n = 2
        elif tabuleiro[3] == simboloComputador and tabuleiro[9] == simboloComputador and tabuleiro[6] == " ":
            n = 6
        elif tabuleiro[9] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[8] == " ":
            n = 8
        elif tabuleiro[1] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[4] == " ":
            n = 4         
        if tabuleiro[5] == simboloJ:
            if tabuleiro[1] == tabuleiro[4] == simboloComputador and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[2] == tabuleiro[1] == simboloComputador and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[3] == tabuleiro[6] == simboloComputador and tabuleiro[9] == " ":
                n = 9
            elif tabuleiro[7] == tabuleiro[8] == simboloComputador and tabuleiro[9] == " ":
                n = 9
            if tabuleiro[2] == simboloJ and tabuleiro[8] == " ":
                n = 8
            elif tabuleiro[6] == simboloJ and tabuleiro[4] == " ":
                n = 4
            elif tabuleiro[4] == simboloJ and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[8] == simboloJ and tabuleiro[2] == " ":
                n = 2
            elif tabuleiro[7] == simboloJ and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[1] == simboloJ and tabuleiro[9] == " ":
                n = 9
            elif tabuleiro[3] == simboloJ and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[9] == simboloJ and tabuleiro[1] == " ":
                n = 1
            elif tabuleiro[9] == simboloJ and tabuleiro[1] == simboloComputador and tabuleiro[4] == " ":
                n = 4
            else:
                n = lastplay(tabuleiro)
    #<----------- quarta rodada rodada ------------>
    elif v == 4:#Pc primeiro
        if tabuleiro[5] == " ":
            #conferir as possibilidades de vitoria com as diagonais
            n = 5
        elif tabuleiro[7] == tabuleiro[9] == simboloJ and tabuleiro[8] == " ":
            n = 8
        elif tabuleiro[5] == simboloComputador:
            if (tabuleiro[8] == simboloComputador or tabuleiro[1] == tabuleiro[3] == simboloComputador) and tabuleiro[2] == " ":
                n = 2
            elif tabuleiro[4] == simboloComputador and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[3] == simboloComputador and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[3] == simboloComputador and tabuleiro[9] == " ":
                n = 9
            elif tabuleiro[9] == tabuleiro[3] == simboloJ and tabuleiro[6] == " ":
                n = 6
            else:
                n = lastplay(tabuleiro)
        elif tabuleiro[5] == simboloJ:
            if tabuleiro[8] == tabuleiro[7] == simboloComputador and tabuleiro[9] == " ":
                n = 9
            elif tabuleiro[8] == tabuleiro[9] == simboloComputador and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[7] == tabuleiro[8] == simboloJ and tabuleiro[9] == " ":
                n = 9
            elif tabuleiro[1] == tabuleiro[9]== simboloComputador and tabuleiro[5] == " ":
                n = 5
            elif tabuleiro[1] == tabuleiro[3] == simboloComputador and tabuleiro[2] == " ":
                n = 2
            elif tabuleiro[3] == tabuleiro[9] == simboloComputador and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[7] == tabuleiro[1] == simboloComputador and tabuleiro[4] == " ":
                n = 4
            elif tabuleiro[9] ==  simboloJ and tabuleiro[1] == " ":
                n = 1
            elif tabuleiro[3] ==  simboloJ and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[1] ==  simboloJ and tabuleiro[9] == " ":
                n = 9
            elif tabuleiro[7] ==  simboloJ and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[2] == simboloJ and tabuleiro[8] == " ":
                n = 8
            elif tabuleiro[4] == simboloJ and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[6] == simboloJ and tabuleiro[4] == " ":
                n = 4
            elif tabuleiro[8] == simboloJ and tabuleiro[2] == " ":
                n = 2
            elif tabuleiro[9] == simboloJ and tabuleiro[1] == simboloComputador and tabuleiro[4] == " ":
                n = 4
            elif tabuleiro[7] == tabuleiro[1] == tabuleiro[9] == simboloComputador:
                if tabuleiro[4] == " ":
                    n = 4
                elif tabuleiro[2] == " ":
                    n = 2
            elif tabuleiro[1] == tabuleiro[3] == tabuleiro[9] == simboloComputador:
                if tabuleiro[2] == " ":
                    n = 2
                elif tabuleiro[6] == " ":
                    n = 6
            elif tabuleiro[3] == tabuleiro[9] == tabuleiro[7] == simboloComputador:
                if tabuleiro[6] == " ":
                    n = 6
                elif tabuleiro[8] == " ":
                    n = 8     
             
    elif v == 3: #Jogador primeiro
        if tabuleiro[5] == simboloComputador:
            if tabuleiro[2] == simboloComputador and tabuleiro[8] == " ":
                n = 8
            elif tabuleiro[7] == simboloComputador and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[4] == simboloComputador and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[8] == simboloComputador and tabuleiro[2] == " ":
                n = 2
            elif tabuleiro[4] == simboloJ and tabuleiro[7] == " ":
                n = 7
            elif tabuleiro[6] == simboloJ and tabuleiro[9] == " ":
                n = 9
            elif tabuleiro[6] == simboloJ and tabuleiro[3] == " ":
                n = 3
            elif tabuleiro[8] == simboloJ and tabuleiro[4] == " ":
                n = 4
            elif tabuleiro[7] == simboloJ == tabuleiro[1] and tabuleiro[4] == " ":
                n = 4
            elif tabuleiro[7] == simboloJ and tabuleiro[6] == " ":
                n = 6
        elif tabuleiro[5] == " ":
            n = 5
        elif tabuleiro[5] == simboloJ:
            if tabuleiro[4] == simboloJ and tabuleiro[6] == " ":
                n = 6
            elif tabuleiro[8] == simboloJ and tabuleiro[2] == " ":
                n = 2 
            elif tabuleiro[6] == simboloJ and tabuleiro[4] == " ":
                n = 4
            elif tabuleiro[2] == simboloJ and tabuleiro[8] == " ":
                n = 8
            elif tabuleiro[9] == simboloJ and tabuleiro[1] == " ":
                n = 1 
            elif tabuleiro[7] == simboloJ and tabuleiro[3] == " ":
                n = 3 
            elif tabuleiro[3] == simboloJ and tabuleiro[7] == " ":
                n = 7
            else:
                n = lastplay(tabuleiro)
                
    #<----------- ultima rodada rodada rodada ------------>               
    elif v == 2:#Pc primeiro
        n = lastplay(tabuleiro)
        

    if n == None or tabuleiro[n] != " " : # #se algo der errado, ele faz uma jogada válida, infelizmente aleatória, mas válida
        n = lastplay(tabuleiro)
        
    # print(v) #com esses dois prints é possivel analisar em qual parte o bot está fazendo determinada acção, afim de poder aprimorá-lo 
    # print(n)
    return n 
    
        
def jogo(primeiro, simboloJ, li = [" "] * 10): #
    """Executa o jogo"""

    if simboloJ == "X":
        simbolo = "O"
    else:
        simbolo = "X"

    #agora pede a jogada
    if primeiro == 1:
        ptabuleiro(li)
        J = jogada(li)
        lista1 =  tabuleiro(simboloJ, J, li)
        if fim(lista1) == "Jogo nao acabou":
            jogadapc = jogadaComputador(lista1, simbolo)
            lista2 = tabuleiro(simbolo, jogadapc, lista1)
        else:
            lista2 = lista1 #preciso fazer essa conversão para no final ele usar a lista certa        
    else:
        jogadapc = jogadaComputador(li, simbolo)
        lista1 = tabuleiro(simbolo, jogadapc, li)
        ptabuleiro(lista1)
            
        if fim(lista1) == "Jogo nao acabou":
            J = jogada(lista1)
            lista2 =  tabuleiro(simboloJ, J, lista1)
        else:
            lista2 = lista1
    
    if fim(lista2) == "Jogo nao acabou":
        return jogo(primeiro, simboloJ, lista2)
    else:
        limpaTela() # para deixar apenas o print do tabuleiro e as informações
        print("Fim!")
        if fim(lista2) == simboloJ:
            ptabuleiro(lista2)
            print("Vitória do Jogador!")
            print("Anotnieta: Parabéns! Dá próxima farei melhor! ")
        elif fim(lista2) == simbolo:
            ptabuleiro(lista2)
            print("Vitória do Computador")
            print("Antonieta: Mais sorte da próxima vez!")
        else:
            ptabuleiro(lista2)
            print("Empate!")

def main():
    
    limpaTela()
    print("Seja bem vindo ao clássico jogo da velha!")
    print("Você vai jogar contra Antonieta, nossa velha mais sagaz!")
    print("Antonieta: oi! Vai um biscoitinho?")
    escolha = validade("Escolha seu simbolo X ou O: ", "Apenas os simbolos x e o são aceitos!", str)
    o = first()
    if o == 1:
        print("Jogador começa primeiro")
    else:
        print("Computador começa primeiro")
    jogo(o, escolha)

    #Você pode, se quiser, comentar os dois prints abaixo:
    print(getNome())
    print(getMatricula())


################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()
