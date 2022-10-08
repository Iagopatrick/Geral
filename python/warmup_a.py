

from posixpath import split


def confere(a, b,x = 1):
    
    for i in a:
        for j in b:
            if i != j:
                return False
    return True

def main():
    principal  = str(input())
    secundaria  = str(input())
    
    a = list(split(principal))
    b = list(split(secundaria))
    
    
    print(f"{confere(a, b)}")
    

main()
