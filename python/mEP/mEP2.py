A = int(input())
B = int(input())
C = int(input())
trainguloexiste = False

if (A == 0 or B == 0 or C == 0) or (A < 0 or B < 0 or C < 0):
    print("Valores invalidos.")
    trainguloexiste = False
elif (A == B + C or B == A + C or C == B + A) or (A > B + C or B > A + C or C > B + A):
    print("Valores nao podem formar um triangulo.")
    trainguloexiste = False
else:
    # equilatero
    if A == B and C == B:
        print("Triangulo equilatero.")
        trainguloexiste = True
    # Isoceles
    elif (A == B and A != C) or (A == C and A != B) or (C == B and C != A) or (B == A and B != C):
        print("Triangulo isosceles.")
        trainguloexiste = True
    # Escaleno
    else:
        print("Triangulo escaleno.")
        trainguloexiste = True

if trainguloexiste == True:    
    if (A >= B and A >= C and A**2 == B**2 + C**2) or (B >= A and B >= C and B**2 == A**2 + C**2) or (C >= A and C >= B and C**2 == B**2 + A**2):
        print("Triangulo retangulo.")
            
    elif (A >= C and A >= B and A**2 < B**2 + C**2) or (B >= A and B >= C and B**2 < A**2 + C**2) or (C >= A and C >= B and C**2 < B**2 + A**2) : 
        print("Triangulo acutangulo.")
            
    elif (A >= C and A >= B and A**2 >= B**2 + C**2) or (B >= A and B >= C and B**2 >= A**2 + C**2) or (C >= A and C >= B and C**2 >= B**2 + A**2):
        print("Triangulo obtusangulo.")
        

