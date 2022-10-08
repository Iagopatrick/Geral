print("-"*35)
print("101 - Batata List          - R$4.50")
print("305 - Suco Py              - R$2.00")
print("248 - Suco Interpretado    - R$4.25")
print("389 - Guaraná Lambda       - R$3.50")
print("145 - Sanduiche Integral   - R$9.00")
print("567 - Cerveja Derivada     - R$8.50")
print("673 - Vitamina Compilada   - R$7.80")
print("-"*35)
produto = int(input("Escolha seu produto: "))
valido = False
#Complete o código
#O objetivo é verificar se o código do produto lido é válido e, caso seja, 
# imprimir o produto escolhido e o seu preço. Caso seja escolhido 
# um produto inválido, exibir uma mensagem de erro.

if produto == 101 :
    print("101 - Batata List          - R$4.50")
    valido = True
elif produto == 305 :
    print("305 - Suco Py              - R$2.00")
    valido = True
elif produto == 248:
    print("248 - Suco Interpretado    - R$4.25")
    valido = True
elif produto == 389:
    print("389 - Guaraná Lambda       - R$3.50")
    valido = True
elif produto == 145:
    print("145 - Sanduiche Integral   - R$9.00")
    valido = True
elif produto == 567:
    print("567 - Cerveja Derivada     - R$8.50")
    valido = True
elif produto == 673:
    print("673 - Vitamina Compilada   - R$7.80")
    valido = True

if valido == True:
    print("produto válido")
else:
    print("Produto inválido - digite o código corretamente")