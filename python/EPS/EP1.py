# Preciso fazer uma máquina que venda bebidas do tipo café ou similares
# escolha: 1 chá de hortelã(inglês, que usa leite), 2 ACHOCOLATADO, 3 café expresso, 4 café com leite, 5 capuccino
# 1: HORTELÃ (10G), LEITE EM PÓ(50G), AGUA(180ML), 1 COPO (250ML)             R$ 5,50
# 2: LEITE EM PÓ (50G), AGUA(150ML), CHOCOLATE em pó(20G), 1 COPO (250ML)     R$ 7,00  
# 3: CAFÉ SOLÚVEL (10G), AGUA(200ML), 1 COPO(250ML)                           R$ 3,00 
# 4: CAFÉ SOLÚVEL (10G), AGUA(180ML), LEITE EM PÓ(50G), 1 COPO(250ML)         R$ 4,00
# 5: CAPUCCINO EM PÓ(30G), AGUA(150ML), LEITE EM PÓ(50G), 1 COPO(250ML)       R$ 6,50  
from os import system , name
def limpatela():
    """Limpa o terminal"""
    if name == 'nt':
        system('cls')
    else:  
	    system('clear') 

def pergunta(msg, tipo):
    """Recebe a msg para fazer a pergunta e o tipo esperado para essa pergunta"""
    try: #Tenta fazer a conversão do valor digitado para int
        x = tipo(input(msg))
        if type(x) == str:
            return x
        else:
            if x < 0: #deixa apenas valores positivos como válidos
                print("Você deve digitar um valor positivo!")
                return pergunta(msg, tipo)
            else:
                return x 
    except: 
        print(f"Você deve digitar um valor do tipo: {tipo}")
        return pergunta(msg, tipo)

def finaliza():
    """Finaliza a maquina, reseta a cor e imprime uma mensagem de fim e também limpa o terminal"""
    RST     = '\033[00m'
    limpatela()
    print("Obrigado, volte sempre :)")
    print(RST)
    exit() 

def menu():
    """Mostra uma tabela sobre as opções do comprador"""
    CYAN    = '\033[36m'
    RST     = '\033[00m'
    cima = "+" + "~" * 50 + "+" #mais fácil padronizar essa parte
    print(CYAN) #Muda a cor da fonte para ciano
    print(cima)
    print("§    » Produtos (Selecione o número ao lado) «     §")
    print(cima)
    print("§   1 - Chá de Hortelã ................. R$ 5,50   §")
    print("§   2 - Achocolatado   ................. R$ 7,00   §")
    print("§   3 - Café Expresso  ................. R$ 3,00   §")
    print("§   4 - Café com Leite ................. R$ 4,00   §")
    print("§   5 - Capuccino      ................. R$ 6,50   §")
    print(cima)
    print("§    »       Outras Opções        «                §")
    print(cima)
    print("§   6 - Informações dos prdutos                    §")
    print("§   7 - Informações da máquina                     §")
    print("§   8 - Finalizar                                  §")
    print(cima)
    print(RST)#Aqui eu preciso resetar pois a cor padrão do programa é o amarelo, menus seráo em ciano

def leitura(n):
    """Lê a opção e retorna qual é, só aceita valores válidos, de 1 a n """
    YELLOW  = '\033[33m'
    print(YELLOW) #psso deixar amarelo que é o padrão e não preciso do reset
    x = pergunta("Escolha a sua opção: ", int)
    
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
    YELLOW  = '\033[33m'
    print(YELLOW)
    print("---> Chá de Hortelã:")
    print("HORTELÃ        -   10g")
    print("LEITE EM PÓ    -   50g")    
    print("AGUA           - 180Ml")        
    print("1 COPO         -  1un.")
    print("")   
    print("---> Achocolatado:")
    print("LEITE EM PÓ    -   50g")
    print("AGUA           - 150Ml")    
    print("CHOCOLATE EM PÓ  - 20g")        
    print("1 COPO         -  1un.")
    print("")   
    print("---> Café Expresso:")
    print("CAFÉ SOLÚVEL   -   10g")
    print("AGUA           - 200Ml")        
    print("1 COPO         -  1un.")
    print("")       
    print("---> Café com Leite:")
    print("CAFÉ SOLÚVEL   -   10g")
    print("AGUA           - 180Ml")    
    print("LEITE EM PÓ    -   50g")        
    print("1 COPO         -  1un.")
    print("")       
    print("---> Cappuccino:")
    print("CAPPUCCINO EM PÓ - 30g")
    print("LEITE EM PÓ    -   50g")        
    print("AGUA           - 150Ml")    
    print("1 COPO         -  1un.")
    
def troco(n, p):
    """Recebe o valor pago (n) e o custo do produto(p) e imprime o troco"""
    # notas: 100, 50, 20, 10, 5, 2
    # moedas: 1, 0.50, 0.25, 0.10, 0.05, 0.01
    d = n - p #Diferença entre o valor pago e o custo
    if d >= 100:
        print("R$ 100,00")
        return troco(n - 100, p)
    elif d >= 50:
        print("R$ 50,00")
        return troco(n - 50, p)
    elif d >= 20:
        print("R$ 20,00")
        return troco(n - 20, p)
    elif d >= 10:
        print("R$ 10,00")
        return troco(n - 10, p)
    elif d>= 5:
        print("R$ 5,00")
        return troco(n - 5, p)
    elif d >= 2:
        print("R$ 2,00")
        return troco(n - 2, p)
    elif d >= 1:
        print("R$ 1,00")
        return troco(n - 1, p)
    elif d >= 0.5:
        print("R$ 0,50")
        return troco(n - 0.50, p)
    elif d >= 0.25:
        print("R$ 0,25")
        return troco(n - 0.25, p) 
    elif d >= 0.10:
        print("R$ 0,10")
        return troco(n - 0.10, p)  
    elif d >= 0.05:
        print("R$ 0,05")
        return troco(n - 0.05, p)    
    elif d >= 0.01:
        print("R$ 0,01")
        return troco(n - 0.01, p) 
    elif d == 0: #Acaba aqui, caso base, quando não houver diferença entre o dinheiro colocado e o valor do produto
        return 

def entrada(preço, d):
    """Recebe o valor do produto (preço) e o dinheiro colocado (d) e avalia se a quantidade de dinheiro inserida paga o produto,
     depois disso gera o troco com a função troco"""
    
    if d >= preço:
        if d - preço > 0:
            print(f"o preço é: {preço}")
            print(f"Seu troco é: R$ {d - preço}")
        return troco(d, preço)
    else:
        print(f"Valor inserido até agora: {d}, necessário: {preço}")
        p = round(pergunta("Adicione mais dinheiro para chegar ao valor: ", float), 2)
        return entrada(preço, d + p)
    
def geloac():
    """Função que ofere gelo e açúcar ao cliente"""

    CYAN    = '\033[36m'
    RST     = '\033[00m'
    YELLOW  = '\033[33m'

    print(CYAN)
    cima = "+" + "~" * 50 + "+"
    print(cima)
    print("§           » Deseja gelo ou açúcar? «             §")
    print(cima)
    print("§              1 ------- Gelo              1 Cubos §")
    print("§              2 ------- Açúcar            1 Cubos §")
    print("§              3 ------- Não                       §")
    print(cima)
    print(RST)
    x = leitura(3)
    print(YELLOW)
    if x == 1:
        print("Tome seu Gelo")
    elif x == 2:
        print("Tome seus cubos de açúcar")
    else:
        print("OK! Aproveite sua bebida!")
        return 
    z = pergunta("Deseja mais açúcar ou gelo? s/n S/N ", str)
    if z == "s" or z == "S":
        return geloac()
    else:
        print("OK! Aproveite sua bebida!")

def maquina(hortela = 0, leitepo = 0, agua = 0, copo = 0, chocolate = 0, cafe = 0, cappuccino = 0, dinheiro = 0):
    """Faz a leitura da opção do comprador, armazena a quantidade dos ingredientes e faturamento.
    A máquina é responsavel por ogarnizar todas funções e armazena cada gasto ou ganho. é Preciso colocar a quantidade dos ingredientes

    hortela, leite em pó, água, copo, chocolate, café e cappuccino
    """
# preciso que ela receba os valores, faça a conta necessária, tirando os elementos que foram usados, 
# e confira se existe a possibilidade de fazer mais
# preciso tambem fazer o sistema de troco
# caso base finalizar o pedido
    RST     = '\033[00m'
    YELLOW  = '\033[33m'
    RED     = '\033[31m'

    menu()
    print(RST) #ele reseta a cor amarela vinda depois que alguem selecionou as opções 6 ou 7
    print(YELLOW)
    L = leitura(8)
    
    
    if 1 <= L <= 5:
        z = pergunta(f"A sua escolha é {L}, Confirma? S/N s/n ", str)
        if z == "s" or z == "S":
            print(RED) #todos os prints depois disso aparecerão em vermelho, são mensagens que a bebida não está disponível
            if L == 1: #Cada if verifica se é possível fazer as bebidas e cada else retira o ingrediente usado, se necessário
                if hortela - 10 < 0 or leitepo - 50 < 0 or agua - 180 < 0 or copo - 1 < 0:
                    print("Essa bebida não está disponivel")
                    return maquina(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino, dinheiro)
                else:
                    hortela -= 10 
                    leitepo -= 50
                    agua -= 180
                    copo -= 1
                    preço = 5.5
            elif L == 2:
                if leitepo - 50 < 0 or agua - 150 < 0 or copo - 1 < 0 or chocolate - 20 < 0:
                    print("Essa bebida não está disponivel")
                    return maquina(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino, dinheiro)
                else:
                    leitepo -= 50 
                    agua -= 150 
                    copo -= 1 
                    chocolate -= 20
                    preço = 7
            elif L == 3:
                if agua - 200 < 0 or copo - 1 < 0 or cafe - 10 < 0:
                    print("Essa bebida não está disponivel")
                    return maquina(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino, dinheiro)
                else:
                    agua -= 200
                    copo -= 1
                    cafe -= 10
                    preço = 3
            elif L == 4: 
                if leitepo - 50 < 0 or agua - 180 < 0 or copo - 1 < 0 or cafe - 10 < 0:
                    print("Essa bebida não está disponivel")
                    return maquina(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino, dinheiro)
                else:    
                    leitepo -= 50
                    agua -= 180
                    copo -= 1
                    cafe -= 10
                    preço = 4
            elif L == 5:
                if leitepo - 50 < 0 or agua - 150 < 0 or copo - 1 < 0 or cappuccino - 30 < 0:
                    print("Essa bebida não está disponivel")
                    return maquina(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino, dinheiro)
                else:
                    leitepo -= 50
                    agua -= 150
                    copo -= 1
                    cappuccino -= 30
                    preço = 6.5
            print(YELLOW)        
            d = round(pergunta("Coloque seu dinheiro: ", float), 2)
            entrada(preço, d)
            dinheiro += preço # armazena o dinheiro na maquina
            geloac()
            print(YELLOW)
            _ = pergunta("Deseja retornar ao menu? S/N ou s/n ", str)  
            if _ == "s" or _ == "S":
                limpatela()
                return maquina(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino, dinheiro)
            else:
                finaliza()
        else:
            return maquina(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino, dinheiro)
            
    elif L == 6:
        info()
        x = pergunta("Deseja retornar ao menu? S/N ou s/n ", str)
        if x == "s" or "S":
            limpatela()
            return maquina(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino, dinheiro)
        else:
            finaliza()

    elif L == 7:
        print("O que contém na máquina no momento:")
        print(f"AGUA:                 {agua}ml")    
        print(f"LEITE EM PÓ:          {leitepo}g")    
        print(f"CAPPUCCINO:           {cappuccino}g")    
        print(f"CAFÉ:                 {cafe}g")   
        print(f"COPO:                 {copo}un.")         
        print(f"HORTELÃ:              {hortela}g")
        print(f"CHOCOLATE:            {chocolate}g")
        print(f"FATURAMENTO:          R${dinheiro}")
        x = pergunta("Deseja retornar ao menu? S/N ou s/n ", str)

        if x == "s" or x == "S":
            limpatela()
            return maquina(hortela, leitepo, agua, copo, chocolate, cafe, cappuccino, dinheiro) 
        else:
            finaliza()
    elif L == 8:
        finaliza()
   

def main():
    limpatela()
    maquina(0, 2500, 2000, 1000, 1000, 1000, 1000)
    
main()