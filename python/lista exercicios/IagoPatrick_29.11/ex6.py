contaPar = 0
somaPar = 0
multiPar = 1
# impar
contaImpar = 0
somaImpar = 0
multiImpar = 1

x = int(input("Digite um numero: "))
if x%2 == 0:
	contaPar += 1 #contPar = contPar + 1
	somaPar += x #somaPar = somaPar + x
	multiPar *= x
	
else:
    contaImpar += 1 
    somaImpar += x
    multiImpar *= x

x = int(input("Digite um numero: "))
if x%2 == 0:
	contaPar += 1 
	somaPar += x
	multiPar *= x
else:
    contaImpar += 1 
    somaImpar += x
    multiImpar *= x

x = int(input("Digite um numero: "))
if x%2 == 0:
	contaPar += 1
	somaPar += x
	multiPar *= x
else:
    contaImpar += 1 
    somaImpar += x
    multiImpar *= x

x = int(input("Digite um numero: "))
if x%2 == 0:
	contaPar += 1
	somaPar += x
	multiPar *= x
else:
    contaImpar += 1 
    somaImpar += x
    multiImpar *= x

print(f"Foram digitados {contaPar} números pares e {contaImpar} números ímpares")
print(f"Soma dos números pares: {somaPar} e soma dos números ímpares: {somaImpar}") 
print(f"A multiplicação dos número pares foi {multiPar} e dos números ímpares foi {multiImpar}") 

if contaPar > 0:
	print(f"Média dos números pares: {somaPar/contaPar:.2f}") # :.2f -> para imprimir com duas casas decimais

if contaImpar > 0 :
	print(f"Média dos números ímpares: {somaImpar/contaImpar:.2f}")
