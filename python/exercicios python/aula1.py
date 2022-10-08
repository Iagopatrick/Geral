# print("Digite a nota1:")
nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))
nota3 = float(input("Digite a nota3: "))
frequencia = float(input("Digite a frequencia: "))


print(f"Nome do aluno {nome}")
print("Nota1:", nota1)
print("Nota2:", nota2)
print("Nota3:", nota3)

media = (nota1 + nota2 + nota3)/3
print("Média:", media)
# print("Aprovado por nota?", media > 7)
# print("Prova Final?", media < 7 and frequencia >= 75)
# print("Reprovado por falta?", frequencia < 75)

if frequencia >= 75:
    if media >= 7: 
     print("Aluno aprovado por nota!")
     print(f"Nota do aluno : {media}")
    else:
         print("Aluno está de prova final!")
         notaPF = float(input("Digite a nota final do aluno: "))
         mediaFinal = (media + notaPF)/2
         if mediaFinal >= 5:
             print("APROVADOR POR NOTA")
         else:
             print("REPROVADO POR NOTA")
         print(f"Nota do aluno: {mediaFinal}")     
else:
    print("REPROVADO POR FALTA, SEM DIREITO DE PROVA FINAL")

# if media >= 7: 
#     print("Aluno aprovado por nota!")
# if media < 7: 
#     print("Aluno está de prova final!")
#     print("Prova Final")
print(" -- Fim do programa -- ")
