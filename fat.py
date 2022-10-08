def fat(x):
    if x == 1 or x == 0:
        return 1
    else:
        return  x * fat(x-1)

entrada = [int(j) for j in input().split()]
M = entrada[0]
N = entrada[1]
final = fat(M) + fat(N)
print(final)

while entrada:
    entrada = [int(j) for j in input().split()]
    M = entrada[0]
    N = entrada[1]
    final = fat(M) + fat(N)
    print(final)

