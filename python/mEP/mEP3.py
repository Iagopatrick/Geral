peso = float(input())   
idade = int(input()) 
if 16 <= idade < 18:  
    doc = str(input())                     
saude = str(input())   
drogas = str(input())  
pD = str(input())
if pD == "N":     
    mesesD = int(input())              
    anoD = int(input())              
sexoB = str(input())              
if sexoB == "F":
    gravidez = str(input())             
    amamentando = str(input())
    if amamentando == "S":
        idadeBB = int(input())


# 1 Peso :
print(f"Peso: {peso}")
# 2 Idade :
print(f"Idade: {idade}")
# 3 Documento de autorizacao :
if 16 <= idade < 18:
    print(f"Documento de autorizacao: {doc}")
# 4 Boa saude :
print(f"Boa saude: {saude}")
# 5 Uso drogas injetaveis :
print(f"Uso drogas injetaveis: {drogas}")
# 6 Primeira doacao :
print(f"Primeira doacao: {pD}")
# 7 Meses desde ultima doacao :
if pD == "N":
    print(f"Meses desde ultima doacao: {mesesD}")
 # 8 Doacoes nos ultimos 12 meses :
    print(f"Doacoes nos ultimos 12 meses: {anoD}")
# 9 Sexo biologico :
print(f"Sexo biologico: {sexoB}")
# 10 Gravidez :
if sexoB == "F":
    print(f"Gravidez: {gravidez}")
 # 11 Amamentando :
    print(f"Amamentando: {amamentando}")
 # 12 Meses bebe :              
    if amamentando == "S":
        print(f"Meses bebe: {idadeBB}")



impedimento = False
# 1 Impedimento : abaixo do peso minimo .
if peso < 50:
    print("Impedimento: abaixo do peso minimo.")
    impedimento = True
# 2 Impedimento : menor de 16 anos .
if idade < 16:
    print("Impedimento: menor de 16 anos.")
    impedimento = True

# 3 Impedimento : menor de 18 anos , sem consentimento dos responsaveis .
if 16 <= idade < 18:
    if doc == "N":
        print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
        impedimento = True
# 4 Impedimento : maior de 60 anos , primeira doacao .
if idade > 60 and pD == "S":
    print("Impedimento: maior de 60 anos, primeira doacao.")
    impedimento = True
# 5 Impedimento : maior de 69 anos .
if idade > 69:
    print("Impedimento: maior de 69 anos.")
    impedimento = True
# 6 Impedimento : nao esta em boa saude .
if saude == "N":
    print("Impedimento: nao esta em boa saude.")
    impedimento = True
# 7 Impedimento : uso de drogas injetaveis .
if drogas == "S":
    print("Impedimento: uso de drogas injetaveis.")
    impedimento = True
if pD == "N":
# 8 Impedimento : intervalo minimo entre as doacoes nao foi respeitado .
    if sexoB == "F" and mesesD < 3:
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        impedimento = True
    elif sexoB == "M" and mesesD < 2:
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        impedimento = True
    # 9 Impedimento : numero maximo de doacoes anuais foi atingido .
    if sexoB == "F" and anoD >= 3:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        impedimento = True
    elif sexoB == "M" and anoD >= 4:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        impedimento = True
if sexoB == "F":
    # 10 Impedimento : gravidez .
    if sexoB == "F" and gravidez == "S":
        print("Impedimento: gravidez.")
        impedimento = True
    # 11 Impedimento : amamentacao .
    if sexoB == "F" and amamentando == "S" and idadeBB < 12:
        print("Impedimento: amamentacao.")
        impedimento = True
if impedimento == False:
    print("Procure um hemocentro.")