def f1(n, m):
    if n <= m:
        print("Ida: ", n)
        f1(n + 1, m)
        print("Volta: ", n)
		
def f2(n, m):
    if n > m:
        return # mesmo que return None
    else:
        print(n)
        f2(n + 1, m)

def f3(n, m):
    print(n)
    if n == m:
        return None 
    f3(n + 1, m)

def f4(n, m):
    print(n)
    if n != m:
        f4(n + 1, m)

def f5(n, m):
    if n <= m:
        print(n)
        f5(n + 1, m)

def main():
    print("f1(20, 10)")
    f1(20, 10)
    print("f2(20, 10)")
    f2(20, 10)
    # print("f3(20, 10)")
    # f3(20, 10)
    # print("f4(20, 10)")
    # f4(20, 10)
    print("f5(20, 10)")
    f5(20, 10)

main()