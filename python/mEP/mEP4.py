
def hora(minutos):
    """ Converte minutos em horas e minutos"""
    hora = minutos//60
    min = minutos%60
    return f"{hora:02d}h {min:02d}min"

def lista(idade, valor, sexo):
    """Lista para saber se o canditado conseguiu o indice necessário com base na idade e sexo.
    É necessário atribuir a idade, o tempo feito e o sexo do candidato ou candidata.
    """
    tn = False
    if sexo == "M" or "m":
        if 18 <= idade <= 34 and valor <= 180:
            tn = True
        elif 35 <= idade <= 39 and valor <= 185:
            tn = True
        elif 40 <= idade <= 44 and valor <= 190:
            tn = True
        elif 45 <= idade <= 49 and valor <= 200:
            tn = True
        elif 50 <= idade <= 54 and valor <= 205:
            tn = True
        elif 55 <= idade <= 59 and valor <= 215:
            tn = True
        elif 60 <= idade <= 64 and valor <= 230:
            tn = True
        elif 65 <= idade <= 69 and valor <= 245:
            tn = True    
        elif 70 <= idade <= 74 and valor <= 260:
            tn = True
        elif 75 <= idade <= 79 and valor <= 275:
            tn = True    
        elif idade > 80 and valor <= 290:
            tn = True
        
        
    if sexo == "f" or sexo == "F":
        if 18 <= idade <= 34 and valor <= 210:
            tn = True
        elif 35 <= idade <= 39 and valor <= 215:
            tn = True
        elif 40 <= idade <= 44 and valor <= 220:
            tn = True
        elif 45 <= idade <= 49 and valor <= 230:
            tn = True
        elif 50 <= idade <= 54 and valor <= 235:
            tn = True
        elif 55 <= idade <= 59 and valor <= 245:
            tn = True
        elif 60 <= idade <= 64 and valor <= 260:
            tn = True
        elif 65 <= idade <= 69 and valor <= 275:
            tn = True    
        elif 70 <= idade <= 74 and valor <= 290:
            tn = True
        elif 75 <= idade <= 79 and valor <= 305:
            tn = True    
        elif idade > 80 and valor <= 320:
            tn = True

    if tn == False:
            return "Conseguiu indice? NAO"
    else:
            return "Conseguiu indice? SIM"

def temponec(idade, sexo, valor):
    """Imprime o tempo do corredor ou corredora e define o tempo necessário, com base na idade e sexo, e retorna
    a quantidade de minutos necessário para a categoria em 'Tempo necessario: xxh xxmin'. 
    idade = idade, sexo = sexo biológico, valor = Minutos feitos"""
    if sexo == "f" or sexo == "F":
        print(f"Tempo da corredora: {hora(valor)}")
        if 18 <= idade <= 34:
            return "Tempo necessario: 03h 30min"
        elif 35 <= idade <= 39:
            return "Tempo necessario: 03h 35min"
        elif 40 <= idade <= 44:
            return "Tempo necessario: 03h 40min"
        elif 45 <= idade <= 49:
            return "Tempo necessario: 03h 50min"
        elif 50 <= idade <= 54:
            return "Tempo necessario: 03h 55min"
        elif 55 <= idade <= 59:
            return "Tempo necessario: 04h 05min"
        elif 60 <= idade <= 64:
            return "Tempo necessario: 04h 20min"
        elif 65 <= idade <= 69:
            return "Tempo necessario: 04h 35min"
        elif 70 <= idade <= 74:
            return "Tempo necessario: 04h 50min"
        elif 75 <= idade <= 79:
            return "Tempo necessario: 05h 05min"   
        elif idade > 80:
            return "Tempo necessario: 05h 20min"
    else:
        print(f"Tempo do corredor: {hora(valor)}")
        if 18 <= idade <= 34:
           return "Tempo necessario: 03h 00min"
        elif 35 <= idade <= 39:
            return "Tempo necessario: 03h 05min"
        elif 40 <= idade <= 44:
            return "Tempo necessario: 03h 10min"
        elif 45 <= idade <= 49:
            return "Tempo necessario: 03h 20min"
        elif 50 <= idade <= 54:
            return "Tempo necessario: 03h 25min"
        elif 55 <= idade <= 59:
            return "Tempo necessario: 03h 35min"
        elif 60 <= idade <= 64:
            return "Tempo necessario: 03h 50min"
        elif 65 <= idade <= 69:
            return "Tempo necessario: 04h 05min"   
        elif 70 <= idade <= 74:
            return "Tempo necessario: 04h 20min"
        elif 75 <= idade <= 79:
            return "Tempo necessario: 04h 35min"  
        elif idade > 80:
            return "Tempo necessario: 04h 50min"

def minutos(idade, sexo, valor):
    """retorna a diferença entre o tempo do corredor(a) e o tempo necessário para a categoria"""
    if sexo == "f" or sexo == "F":
        if 18 <= idade <= 34:
            x = 210
        elif 35 <= idade <= 39:
            x = 215
        elif 40 <= idade <= 44:
            x = 220
        elif 45 <= idade <= 49:
            x = 230
        elif 50 <= idade <= 54:
            x = 235
        elif 55 <= idade <= 59:
            x = 245
        elif 60 <= idade <= 64:
            x = 260
        elif 65 <= idade <= 69:
            x = 275
        elif 70 <= idade <= 74:
            x = 290
        elif 75 <= idade <= 79:
            x = 305   
        elif idade > 80:
            x = 320
    else:
        if 18 <= idade <= 34:
           x = 180
        elif 35 <= idade <= 39:
            x = 185
        elif 40 <= idade <= 44:
            x = 190
        elif 45 <= idade <= 49:
            x = 200
        elif 50 <= idade <= 54:
            x = 205
        elif 55 <= idade <= 59:
            x = 215
        elif 60 <= idade <= 64:
            x = 230
        elif 65 <= idade <= 69:
            x = 245   
        elif 70 <= idade <= 74:
            x = 260
        elif 75 <= idade <= 79:
            x = 275  
        elif idade > 80:
            x = 290
    real = x - valor
    indice = abs(real)
    if sexo == "m" or sexo == "M":
        if real >= 0:
            return f"O corredor correu {hora(indice)} abaixo do indice"
        elif real < 0:
            return f"O corredor correu {hora(indice)} acima do indice"
    if sexo == "f" or sexo == "F":
        if real >= 0:
            return f"A corredora correu {hora(indice)} abaixo do indice"
        elif real < 0:
            return f"A corredora correu {hora(indice)} acima do indice"

def main():
    min = int(input())
    idade = int(input())
    sexo = input()
    print(temponec(idade, sexo, min))
    print(lista(idade, min, sexo))
    print(minutos(idade, sexo, min))

main()
