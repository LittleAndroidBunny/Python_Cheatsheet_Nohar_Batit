 # 1.
# Get first and last name and print them last, first
print("Exercise 1:")
FN = input("Please enter your first name: ")
LN = input("Please enter your last name: ")
print(LN, FN)
# 2.
#Get a number from user and print the unity
print("Exercise 2:")
num = float(input("Please enter a number "))
print(int(num) % 10)
# 3.
# get a string from user and print it, the first letter should be at place 70
print("Exercise 3:")
string = input("Type anything: ")
print(" " * 69 + string)
# 4.
# get a string from user and print it, the last letter should be at place 70
print("Exercise 4:")
string = input("Type anything: ")
print((70 - len(string)) * " " + string)
# 5.
#get two numbers from user and say if they are equal or not
print("Exercise 5:")
num1 = float(input("Please enter the first number: "))
num2 = float(input(("Please enter the second number: ")))
print("The statement that the two numbers are equal is", num1 == num2)
# 6.
#get a number from user and print if even
print("Exercise 6:")
num = float(input("Please enter a number: "))
print("The statement that the number", num, "is even, is", num % 2 == 0)
