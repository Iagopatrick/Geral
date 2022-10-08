jogador1 = input("Você quer ser X ou O? ")
if jogador1 == "X" or jogador1== "x":
    print("jogador1: X e jogador2: O")
    jogador2 = "O"
elif jogador1 == "O" or jogador1 == "o":
    print("jogador1: O e jogador2: X")
else:
    print("ERRO - SELECIONE APENAS 'X' OU 'O'")