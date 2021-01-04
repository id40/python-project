import random
import colorama

print(colorama.Back.BLACK)

x = 0

while(1):
    for y in range(1, 75):
        print(random.randint(1, 7), end="")
        x = x+1
    print("")
    if (x % random.randint(50, 100) == 0):
        print(colorama.Fore.RED)
    else:
        print(colorama.Fore.BLUE)
