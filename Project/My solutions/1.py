#############################
########FIRST PROJECT########
#        Nohar Batit        #
##        315572941        ##
#############################

#1 We'll write a program that gets the full name of the user, as two strings, and prints the last name,and
# then the first name
name = input("Please enter your first name:\n")
surName = input("Please enter your last name:\n")
print(f"Hello, {surName} {name}.\n")
#2 We'll write a program that gets a number as an input, and printing only the last digit of the number
num1 = float(input("Please enter a number:\n"))
last_digit = int(abs(num1) % 10)
print(f"The last digit in the number {num1} is: {last_digit}.\n")
#3 We'll get a string as an input, and print the first letter at the 70th column
str3 = str(input("Please enter a string:\n"))
print(" "*69+str3)
#4 We'll print the string that we're getting from the user, such that the last letter will be at the 70th column
str4 = str(input("Please enter a string:\n"))
str4_new = 70 - len(str4)
print(" "* str4_new+str4)
#5 We'll define 2 variables and get the inputs from the user by clicking "enter" between their inputs
#Then, we'll compare between them, and print the true/false statement
a, b = int(input("Please enter two numbers:\n")), int(input(""))
c = a == b
print(f"The statement {a} = {b} is: {c}.\n")
#6 We'll ask from to user a number to check it's duality
x = int(input("Please enter a number:\n"))
duality = abs(x % 2) == 0
print(f"The answer regarding the duality of the number {x} is: {duality}.")
print("Bye bye!")
