# Preciso fazer uma máquina que venda bebidas do tipo café ou similares
# escolha: 1 chá de hortelã(inglês, que usa leite), 2 ACHOCOLATADO, 3 café expresso, 4 café com leite, 5 capuccino
# 1: HORTELÃ (10G), LEITE EM PÓ(50G), AGUA(180ML), 1 COPO (250ML)             R$ 5,50
# 2: LEITE EM PÓ (50G), AGUA(150ML), CHOCOLATE BARRA(20G), 1 COPO (250ML)     R$ 7,00  
# 3: CAFÉ SOLÚVEL (10G), AGUA(200ML), 1 COPO(250ML)                           R$ 3,00 
# 4: CAFÉ SOLÚVEL (10G), AGUA(180ML), LEITE EM PÓ(50G), 1 COPO(250ML)         R$ 4,00
# 5: CAPUCCINO EM PÓ(30G), AGUA(150ML), LEITE EM PÓ(50G), 1 COPO(250ML)       R$ 6,50  
from os import system , name
def limpatela():
    if name == 'nt':
        system('cls')
    else:  
	    system('clear') 


def menu():
    CYAN    = '\033[36m'
    RST     = '\033[00m'
    cima = "+" + "-" * 50 + "+"
    print(CYAN)
    print(cima)
    print("|      Produtos (Selecione o número ao lado)       |")
    print(cima)
    print("|   1 - Chá de Hortelã ................. R$ 5,50   |")
    print("|   2 - Achocolatado   ................. R$ 7,00   |")
    print("|   3 - Café Expresso  ................. R$ 3,00   |")
    print("|   4 - Café com Leite ................. R$ 4,00   |")
    print("|   5 - Capuccino      ................. R$ 6,50   |")
    print(cima)
    print("|                  Outras Opções:                  |")
    print(cima)
    print("|   6 - Informações dos prdutos                    |")
    print("|   7 - Informações da máquina                     |")
    print("|   8 - Finalizar                                  |")
    print(cima)
    print(RST)

def leitura(n):
    """Lê a opção e retorna qual é, só aceita valores válidos, de 1 a n """
    x = int(input("Escolha a sua opção: "))
    
    if 1 <= x <= n:
        return x
    else:
        print("Digite valores válidos!")
        return leitura(n)

def info():
    """
    Mostra na tela os ingredientes necessários para cada bebida da máquina e depois pergunta se o cliente quer
    voltar ao menu ou finalizar
    """
    print("Chá de Hortelã:")
    print("HORTELÃ        -   10g")
    print("LEITE EM PÓ    -   50g")    
    print("AGUA           - 180Ml")        
    print("1 COPO         -  1un.")
    print("")   
    print("Achocolatado:")
    print("LEITE EM PÓ    -   50g")
    print("AGUA           - 150Ml")    
    print("CHOCOLATE BARRA  - 20g")        
    print("1 COPO         -  1un.")
    print("")   
    print("Café Expresso:")
    print("CAFÉ SOLÚVEL   -   10g")
    print("AGUA           - 200Ml")        
    print("1 COPO         -  1un.")
    print("")       
    print("Café com Leite:")
    print("CAFÉ SOLÚVEL   -   10g")
    print("AGUA           - 180Ml")    
    print("LEITE EM PÓ    -   50g")        
    print("1 COPO         -  1un.")
    print("")       
    print("Cappuccino:")
    print("CAPPUCCINO EM PÓ - 30g")
    print("LEITE EM PÓ    -   50g")        
    print("AGUA           - 150Ml")    
    print("1 COPO         -  1un.")
    x = input("Deseja retornar ao menu? S/N ou s/n")
    if x == "s" or "S":
        return()
    else:
        exit()

def preco(n, x = 0):
    if n == 1:
        return x + 5.5
    elif n == 2: 
        return x + 7
    elif n == 3:
        return x + 3
    elif n == 4:
        return x + 4
    elif n == 5:
        return x + 6.5


def maquina(hortela = 0, leitepo = 0, agua = 0, copo = 0, chocolate = 0, cafe = 0, cappuccino = 0, dinheiro = 0):
    """Faz as contas do que foi gasto"""
    L = leitura(8)
    if 1 <= L <= 5:
        if L == 1:
            
            if hortela - 10 < 0 or leitepo - 50 < 0 or agua - 180 < 0 or copo - 1 < 0:
                return "Essa bebida não está disponivel"
            else:
                return hortela - 10, leitepo - 50, agua - 180, copo -1, chocolate, cafe, cappuccino
        elif L == 2:
            
            if leitepo - 50 < 0 or agua - 150 < 0 or copo - 1 < 0 or chocolate - 20 < 0:
                return "Essa bebida não está disponivel"
            else:
                return hortela, leitepo - 50, agua - 150, copo -1, chocolate - 20, cafe, cappuccino
        elif L == 3:
            
            if agua - 200 < 0 or copo - 1 < 0 or cafe - 10 < 0:
                return "Essa bebida não está disponivel"
            else:
                return hortela, leitepo, agua - 200, copo -1, chocolate, cafe - 10, cappuccino
        elif L == 4:
            
            if leitepo - 50 < 0 or agua - 180 < 0 or copo - 1 < 0 or cafe - 10 < 0:
                return "Essa bebida não está disponivel"
            else:    
                return hortela, leitepo - 50, agua - 180, copo -1, chocolate, cafe - 10, cappuccino
        elif L == 5:
            
            if leitepo - 50 < 0 or agua - 150 < 0 or copo - 1 < 0 or cappuccino - 30 < 0:
                return "Essa bebida não está disponivel"
            else:
                return hortela, leitepo - 50, agua - 150, copo -1, chocolate, cafe, cappuccino - 30
    elif L == 6:
        info()
    elif L == 7:
        print("O que contém na máquina no momento:")
        print(f"AGUA:                     {agua}ml")    
        print(f"LEITE EM PÓ:            {leitepo}g")    
        print(f"CAPPUCCINO:          {cappuccino}g")    
        print(f"CAFÉ:                      {cafe}g")   
        print(f"COPO:                    {copo}un.")         
        print(f"HORTELÃ:                {hortela}g")
        print(f"CHOCOLATE:            {chocolate}g")
        print(f"FATURAMENTO:          R${dinheiro}")
        x = input("Deseja retornar ao menu? S/N ou s/n")
        if x == "s" or "S":
            return maquina()
        else:
            exit()
    elif L == 8:
        print
        exit()
        
        
# def maquina(hortela = 0, leitepo = 0, agua = 0, copo = 0, chocolate = 0, cafe = 0, cappuccino = 0):
#     h, l, a, c, cho, ca, cap = conta(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino)
#     # preciso que ela receba os valores, faça a conta necessária, tirando os elementos que foram usados, 
#     # e confira se existe a possibilidade de fazer mais
#     # preciso tambem fazer o sistema de troco
#     # caso base finalizar o pedido
    

#     print()
def main():
    menu()
    maquina(200, 100, 100, 100, 100, 100, 100)
main()