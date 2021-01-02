print("Welcome! To Basic Calculator")

runAgain = 1
# this loop is used to run the task again and again
while(runAgain):
    print("\nMENU")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    x = int(input("Enter your Choice (select any given number): "))
    print("\n")

    # this if is used to state for wrong choice
    if x > 4:
        print("\nYou have entered wrong choice!!")
        runAgain = input(
            "\nDo you want to run this program again (1 -> Yes, 0 -> No): ")
    else:
        z = int(input("Enter First number: "))
        y = int(input("Enter Second number: "))

        # this if is used to perform mathemathical task
        if x == 1:
            print("\nAddition of", z, "and", y, "is", z + y)
        elif x == 2:
            print("\nSubstraction of", z, "and", y, "is", z - y)
        elif x == 3:
            print("\nMultiplication of", z, "and", y, "is", z * y)
        elif x == 4:
            print("\nDivision of", z, "and", y, "is", z / y)
        runAgain = input(
            "\nDo you want to run this program again (1 -> Yes, 0 -> No): ")
