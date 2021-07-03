#######################
###  Nohar_Batit    ###
###   315572941     ###
#######################

#################################
# Exercise 1: This function gets an integer from the user,
# and prints if it's divides by either 2 or 3, or both.
def func_div23(x):
    try:
        int(x)
        x = int(x)
        if x == 0:
            return f"The number {int(x)} divides by 2"
        elif abs(x % 6) == 0:
            return f"The number {int(x)} divides by 2,3"
        elif abs(x % 2) == 0:
            return f"The number {int(x)} is divided by 2"
        elif abs(x % 3) == 0:
            return f"The number {int(x)} is divided by 3"
        else:
            return f"The number {int(x)} isn't divisible by 2 nor 3"
    except:
        return func_div23(input("Please enter an integer:\n"))


#################################
# Exercise 3: This function gets 2 numbers, and prints the smallest positive number that is divided by both of them
def smallest_dev(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

#################################
# Exercise 5: This program gets a number and printing two numbers that the result b^c = input while c is in range (6)
#if doesn't exist, prints none
def sqr_func(a):
    try:
        int(a)
        a = int(a)
        if a < 0:
            print(f'The suitable values b, c such that b^c={int(a)} are:')
            print("There are no suitable real values\n")
        elif int(a) == 0:
            print(f'The suitable values b, c such that b^c={int(a)} are:')
            print(f"{int(a)}, any number except zero\n")
        else:
            print(f'The suitable values b, c such that b^c={int(a)} are:')
            for c in range(1, 6):
                b = round(a**(1/c))
                if b**c == a:
                    print(f"{int(b)}, {c}")
                    if c % 2 == 0:
                        print(f"{int(-b)}, {c}")
    except:
        sqr_func(input("Wrong input.Please enter integers only\n"))
################################
# Exercise 6: This program gets a string of numbers and "," between, and calculate the sum of the numbers
def checkstrsum(string):
        try:
            list6 = string.split(",")
            sumlist6 = sum(map(float, list6))
            if sumlist6 != int(sumlist6):
                print(f"The sum of the given numbers is: {sumlist6}")
            else:
                print(f"The sum of the given numbers is: {int(sumlist6)}")
        except:
            checkstrsum(input("Try again. Please enter a list of numbers separated by commas:\n"))


#################################
# Exercise 7: This function gets at least five number from the user, and a replacement number (value and index)
# after that, we'll print the original and new lists, and their sum as a number
list7_1 = []


def list7_original(numbers):
    if numbers == "send" and (len(list7_1) >= 5): #write send and push enter to stop
        return list7_1
    try:
        list7_1.append(float(numbers))
        list7_original(input())
    except ValueError:
        list7_original(input("Wrong input/less than 5 numbers. write 'send' when done:\n"))


def getval(value):
    try:
        float(value)
        return float(value)
    except:
        getval(input("Please choose a number:\n"))

def getindex(ind, le):
    validindex = True
    while validindex:
        try:
            int(ind)
            if le > int(ind):
                validindex = False
            else:
                ind = input("Wrong input.Please choose an index:\n")
        except Exception as e:
            ind = input("Wrong input.Please choose an index:\n")
    return int(ind)

def looplist7(list_):
    for num in range(len(list_)):
        if list_[num] == int(list_[num]):
            list_[num] = int(list_[num])
        else:
            list_[num] = list_[num]

###################################################################################################

####1
print("Exercise 1:\n")
ans1 = func_div23(input("Please enter an integer:\n"))
print(f"{ans1}\n")

####2 ****************************
print("Exercise 2:") #The program gets 3 numbers, and returns the smallest among them.
list2 = []
min_num = 0

counter = 0
while counter < 3:
    try:
        if counter == 0:
            x = list2.append(float(input("Please enter 3 numbers:\n")))
        else:
            x = list2.append(float(input()))
        counter += 1
    except:
        print("Only numbers are allowed")

if min(list2).is_integer():
    min_num = int(min(list2))
else:
    min_num = min(list2)
print(f"The smallest number among the 3 is: {min_num}\n")

####3 ****************************
print("Exercise 3:")
num = 0
x = 0
y = 0
while num < 2:
    try:
        if num == 0:
            x = int(input("Please insert two integers:\n"))
        else:
            y = int(input())
        num += 1
    except:
        print("Please enter integers only")

print(f"The smallest common divisor is| {smallest_dev(x,y)}")

####4 ****************************
print("Exercise 4:\n")
list4 = []
temp = 0
list4_even = []
even_num = 0
j = 0
while j < 20:
    try:
        if j == 0:
            list4.append(int(input("Please enter 20 numbers:\n")))
        else:
            list4.append(int(input()))
        j += 1
    except:
        print("Only numbers are allowed")

for i in range(0, 20):
    if list4[i] % 2 == 0:
        list4_even.append(list4[i])

if list4_even:
    even_num = print(f"The biggest even number is {max(list4_even)}")
else:
    print("There is no even num")

####5 ****************************
print("Exercise 5:\n")
sqr_func(input("Please choose an integer:\n"))

####6 ****************************
print("\n")
print("Exercise 6:\n")
checkstrsum(input("Please enter a list of numbers separated by commas:\n"))

####7 ****************************
print("Exercise 7:\n")
list7_back = list7_original(input("Please enter a list of at least 5 numbers, separated by enter.\nEnter 'send' when done:\n"))
value = getval(input("Please choose a number:\n"))
index_input = input("Please choose an index:\n")
len_list1 = len(list7_1)
index = getindex(index_input, len_list1)
list7 = []
list7 = list7 + list7_1
looplist7(list7)
list7_2 = []
list7_2 = list7_2 + list7_1
list7_2[index] = value
looplist7(list7_2)

print(f"The sum of list 1: {list7} is: {sum(list7)}")
print(f"The sum of list 2: {list7_2} is: {sum(list7_2)}")
