def converte(x):
    hora = x//3600
    min = x%3600//60
    sec = x%60
    print(f"{hora} horas, {min} minutos, {sec} segundos")

def main():
    s = int(input("Digite a quantidade de segundos: "))
    converte(s)

main()