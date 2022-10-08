A = int(input())
B = int(input())
C = int(input())
if (A>100 or A<0) or (C>100 or C<0) or (B>100 or B<0):
    print("Erro, os valores das cartas só podem ser de 0 a 100")
else:
    if A == B:
     print(C)
    else:
     if A == C:
        print(B)
     else:
        if B == C:
            print(A)
            