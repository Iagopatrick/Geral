media = float(input("Digite a média do aluno: "))
if media > 10 or media < 0:
    print("ERRO - APENAS VALORES ENTRE 0 A 10 SÃO PERMITIDOS")
elif media >= 9.0:
    print("A")
elif media >= 8.0:
    print("B")
elif media >= 7.0:
    print("C")
elif media >= 6.0:
    print("D")
else:
    print("R")