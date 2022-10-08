import math as m

def ehNumero(x):
    return True if type(x) == int or type(x) == float else False


def volumeCilindro(r, h):
    
    if ehNumero(h) and ehNumero(r) == True:  
        return m.pi * r**2 * h
    else:
        print("ERRO - OS VALORES DEVEM SER NÚMEROS")
        
def main():
    print(volumeCilindro(1, 3))
    print(volumeCilindro(1, "2"))
main()