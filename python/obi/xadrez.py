L= int(input())
C= int(input())

# if (L <= 0 or L > 1000) or (C < 0 or C > 1000):
#     print("Erro, os valores de L e C devem estar entre 0 e 1000")
# else:
if (L % 2 == 1) and (C % 2 == 1) or (L % 2 == 0) and (C % 2 == 0) :
        print(1)
else:
        if (L % 2 == 1) and (C % 2 == 0) or (L % 2 == 0) and (C % 2 == 1):
          print(0)
