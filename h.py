t = int(input())
listaresultados = []
base = 2
topo = 3

for j in range(t):
    n = int(input())
    for i in range(n):
        # print((n - (topo * (i + 1))) > (n - (topo * (i + 2))))
        # print(".")
        
        if ((n - (topo * (i + 1))) > 0) and ((n - (topo * (i + 1))) > (n - (base * (i + 1)))):
            n -= topo * i
            # print(f"{n} .")
        else:
            x = int(n / 2)
            listaresultados.append(x)
            break


for i in range(t):
    print(listaresultados[i])