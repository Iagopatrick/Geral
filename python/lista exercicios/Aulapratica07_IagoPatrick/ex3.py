def B(n):
    """Descobre o equivalente binario do número decimal n"""
    return 0 if n == 0 else  n%2 + 10 * B(n//2)
        
    
def main():
    print (B(1))
    print (B(2))
    print (B(3))
    print (B(4))
    print (B(5))
    print (B(6))
    print (B(7))
main()