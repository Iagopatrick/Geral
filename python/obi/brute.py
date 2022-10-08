def funtion1(i, o = "1000"):
    
    if i == o:
        return None
    else:
        print(len(i))
        return (i + "1", o)

def lista(n):
    lista19 = ( "one",  "two",  "three", "four",  "five", "six",  "seven", "eight", "nine", "ten",
 "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
"eighteen", "nineteen")
    lista10 = ( "twenty", "thirty", "thirty", "fifty", "sixty", "seventy", "eighty", "ninety", "one hundred")

def main():
    
    x = input("")
    funtion1(x)

main()
