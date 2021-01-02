# importing random class
import random

# it randomly generate the number between one to twenty
x = random.randint(1, 20)

# putting variable value for number of chances
n = 10

print("\n\nHello! Welcome to GUESS AND WIN game \n")

print("GAMES RULES ")

print("1. Rule number one, Guess the number between 1 to 20.")

print("2. Rule number two, You have ", n, " chances.")

# for loop is used to impliment chances
for y in range(1, n+1):

    # num is used to store user input
    num = int(input("\nEnter your Guess: "))

    # this if statement use to warn the user, when they enter value > 20
    if num > (20):
        print("Warning! Please enter the number below or equal to 20.")

    # this if statement is used to check randomly generated number with user input
    if x != num:
        if n-y == 1:
            print("Your guess is wrong! (Last Chance). Try again.")
        elif n-y == 0:
            print("You Loss!!")
        else:
            print("Your guess is wrong! (Chance Left ", n-y, "). Try again.")

    # this else statement will run when user guess correct answer
    else:
        print("Your guess is correct! You WIN.")
        break
