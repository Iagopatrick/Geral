# Treino de lista bolha e busca binaria, diminui a complexidade da vida
l = [1, 3, 4, -5, 100, 25, -7]
# for i in l:
#     print(i)
#     # Range = vai anotar o indice de cada um ex:
# print(list(range(len(l))))

for i in l:
    print(i,end = ",")
print()
# ordena os valores
# l.sort() = ordena os valores  da lista em ordem crescente
sorted(l) # não muda a lista

for i in l:
    print(i,end = ",")
print()


li = sorted(l)

for i in li:
    print(i,end = ",")
print()



listapares =[[0,0], [-2,3], [4,10], [10,10], [20, -1]]
listapares.sort(key = lambda x: x[1]**2)#função lambda é uma função qualquer, key é a chave de parametro. De base, a função sort
# vai ordenar a lista conforme o primeiro valor da lista interta, ou seja, vai olhar o indice 0.
#  map = função de alta ordem que mapea cada elemento e transforma ele em algo ou seja:
lista = list(map(int, input().split()))
print(lista)
print(listapares)