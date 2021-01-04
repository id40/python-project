print("\n\nWelcome to Muliplication Table Generator")
print("========================================\n")

# num variable is used to store data which is used to make a table
num = int(input("Enter the number for Table: "))

# lim variable is used to store data which is used to make a limit of table
lim = int(input("Enter the Limit of the Table: "))

for x in range(1, lim+1):
    print(num, '*', x, '=', num*x)
