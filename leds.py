x = int(input())
leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(x):
    entrada = input()
    led = 0
    for j in range(len(entrada)):
        led += leds[int(entrada[j])]
    print(f"{led} leds")
