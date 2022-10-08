tempo = float(input("Digite o tempo gasto pelo seu programa, em segundos: "))
hora = tempo//3600
minuto = tempo%3600//60
segundos = tempo%60

print(f"{hora} horas: {minuto} minutos: {segundos}segundos")