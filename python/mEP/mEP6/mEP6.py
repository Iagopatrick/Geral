######################################################
# Programação Funcional / Programção I (2021/2)
# miniEP6 - Avatar: A Lenda de Aang
# Nome: IAGO PATRICK DE MELO GRIPP VILAS BOAS
# Matrícula: 2021200087
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do 
#   Paradigma Funcional;
# - Você não pode usar variáveis globais;
# - Caso precise, você PODE criar outras funções;
# - Você PODE adicionar os parâmetros que achar 
#   necessários na função 'realizaTreinamentoAvatar'.
######################################################

def realizaTreinamentoAvatar(agua = 0, fogo = 0, terra = 0, ar = 0):
    """
    Função responsável pela leitura dos dados e cálculo da pontuação do treinamento do Avatar. 
    A função deve retornar True se o treinamento foi realizado com sucesso e False, caso contrário. 
    """
    elemento = input("")

    if elemento == "FIM":
        print("Pontuacao Final")
        print(f"Agua: {'0' if agua < 0 else agua:.1f}")
        print(f"Terra: {'0' if terra < 0 else terra:.1f}")
        print(f"Fogo: {'0' if fogo < 0 else fogo:.1f}")
        print(f"Ar: {'0' if ar < 0 else ar:.1f}")
        if agua <= 0 or fogo <= 0 or terra <= 0 or ar <= 0:
            return False
        else:
            return True
    elif elemento != "FIM":    
        p = int(input(""))
        
        if elemento == "FOGO" :
            fogo = p + fogo
            if agua - p/2 >= 0:
                agua = agua - (p/2)
            else:
                agua = 0           
        elif elemento == "TERRA":
            terra = p + terra
            if ar - (p/2) >= 0:
                ar = ar - (p/2)
            else:
                ar = 0          
        elif elemento == "AGUA":
            agua = p + agua
            if fogo - (p/2) >= 0:
                fogo = fogo - (p/2)
            else:
                fogo = 0        
        elif elemento == "AR":
            ar = p + ar
            if terra - (p/2) >= 0:
                terra = terra - (p/2)
            else:
                terra = 0 
        return realizaTreinamentoAvatar(agua, fogo, terra, ar)
            
    return 

######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
######################################################
def main():
    treinamentoAvatar = realizaTreinamentoAvatar()
    if treinamentoAvatar == True:
        print("Treinamento realizado com sucesso.")
    elif treinamentoAvatar == False:
        print("Realize mais treinamentos.")
    else:
        print("ERRO: A implementação da função 'realizaTreinamentoAvatar' possui algum erro")

main()
