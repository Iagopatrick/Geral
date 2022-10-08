# Uma empresa telefônica oferece planos diferenciados
# de acordo com a quantidade de minutos usados por mês. 
# Abaixo de 200 minutos, a empresa cobra r$ 0,20 por minuto.
# Entre 200 a 400 minutos, o preço é R$ 0,18.
# Acima de 400 minutos, o preço por minuto é de R$ 0,15.
#
min = int(input("Digite a quantidade de minutos: "))
# if min < 0:
#     print("ERRO!")
# if 0 <= min < 200:
#     print(f"Valor da conta: R$ {min * 0.2}")
# if 200 <= min <= 400:
#     print(f"Valor da conta: R$ {min * 0.18}")
# if min > 400:
#     print(f"Valor da conta: R$ {min * 0.15}")
if min < 0:
    print("ERRO!")
else:
    if min < 200:
        print(f"Valor da conta: R$ {min * 0.2}")
    else:
        if min <= 400:
            print(f"Valor da conta: R$ {min * 0.18}")
        else: # min > 400
            if min <= 600:
             print(f"Valor da conta: R$ {min * 0.15}")       
            else:
                if min <= 800:
                 print(f"Valor da conta: R$ {min * 0.12}" )
                else:
                    if min <= 1000:
                        print(f"Valor da conta: R$ {min * 0.9}")
                    else:
                        print(f"Valor da conta: R$ {min * 0.7}")
print("-- Fim do Programa --") 


    