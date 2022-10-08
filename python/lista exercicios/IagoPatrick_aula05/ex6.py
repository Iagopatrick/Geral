def ehNumero(x):
    return True if type(x) == int or type(x) == float else False
def main():
    print(ehNumero(3.001231241431))
    print(ehNumero(13123123243456675141231))
    print(ehNumero(True))
    print(ehNumero("123"))
    print(ehNumero(123))
main()
