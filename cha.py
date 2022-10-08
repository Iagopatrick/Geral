cha = int(input())
entrada = [int(j) for j in input().split()]
competidores =  [x for x in entrada if x == cha]
print(len(competidores))