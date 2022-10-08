from itertools import count
import statistics as s
def main():
    x = input()
    z = list(x)
    b = s.mode(z)
    print(z.count(b))
main()
