def idade(m, a, b):
    
    x =  m - (a + b)
    if a > b and a > x:
        return a
    if b > a and b > x:
        return b
    if x > b and x > a:
        return x        
     


def main():
    m = int(input(""))
    a = int(input(""))
    b = int(input(""))
    print(idade(m, a, b))

main()