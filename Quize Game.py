import random
print("\n\nWelcome to Mathamethical Quize Game\n")
print("\nMENU")
print("----\n")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
num = int(input("\nEnter your Choice (select any given number): "))
print("\n")


score = 0

if num == 1:
    print("Addition")
    print("--------\n")
    for x in range(1, 11):
        y = (random.randint(1, 10))
        z = (random.randint(1, 10))
        print(y, '+', z, '=', end=" ")
        ans = int(input())
        if y+z == ans:
            score = score+1
    print("\nSCORE = ", score)

elif num == 2:
    print("Substraction")
    print("------------\n")
    for x in range(1, 11):
        y = (random.randint(1, 10))
        z = (random.randint(1, 10))
        print(y, '-', z, '=', end=" ")
        ans = int(input())
        if y-z == ans:
            score = score+1
    print("\nSCORE = ", score)

elif num == 3:
    print("Multiplication")
    print("--------------\n")
    for x in range(1, 11):
        y = (random.randint(1, 10))
        z = (random.randint(1, 10))
        print(y, '*', z, '=', end=" ")
        ans = int(input())
        if y*z == ans:
            score = score+1
    print("\nSCORE = ", score)

elif num == 4:
    print("Division")
    print("--------\n")
    for x in range(1, 11):
        y = (random.randint(1, 10))
        z = (random.randint(1, 10))
        print(y, '/', z, '=', end=" ")
        ans = int(input())
        if y/z == ans:
            score = score+1
    print("\nSCORE = ", score)

if score <= 4:
    print("You Failed!!")

elif score == 10:
    print("OutStanding!!")

elif score >= 8:
    print("Great!!")
