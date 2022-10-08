from cmath import sqrt

entrada = [int(j) for j in input().split()]
T = entrada[0]
M = entrada[1]
R = sqrt((4*T)-1)
entrada = [int(j) for j in input().split()]
for i in range(M):
    x = entrada[0]
    if x < entrada[i]:
        x = entrada[i]
    L = x

soma1, soma2 = 0, 0

for i in range(M):
    F = (1/R) * (((1+R)/2)**entrada[i] - ((1-R)/2)**entrada[i])
    soma2 = soma2 + F
    
for j in range(L):
    F = (1/R) * (((1+R)/2)**j - ((1-R)/2)**j)
    soma1 = soma1 + F
final = soma1 - soma2
final2 = abs(final/10**9 + 9)
x = abs(final - ((10**9 + 9) * final2))

print(f"{int(x)}")
# print(x)