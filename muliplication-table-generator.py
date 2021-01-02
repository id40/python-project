# num variable is used to store data which is used to make a table
num = int(input("Enter the number:"))

# lim variable is used to store data which is used to make a limit of table
lim = int(input("Limit of the table:"))

for x in range(1, lim+1):
    print(num, '*', x, '=', num*x)
