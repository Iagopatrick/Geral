x = int(input())
while x != 0:
    entrada = input()
    string = []
    string += [entrada]
    for i in range(x - 1):
        entrada = input()
        string += [entrada]
    # é preciso achar a raiz das palavras
    string.sort(key = len)
    print(string)
    menor = string[0]
    print(f"Aqui estou {menor}")
    contador = 0
    # é preciso de uma estratégia de 'crescimento'
    for j in range(1, len(string)):
        if menor in string[j]:
            print(string[j])
            contador += 1
    print(contador if contador > 2 else len(string))
    x = int(input())