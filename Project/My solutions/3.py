######################
##  Nohar_Batit    ###
##   315572941     ###
######################

################################
def fraction(x):
    if "/" in x:  # In case you want to enter as fraction. used this only when asked specifically, but i could call
        # it wherever it needed. Personally, i think that by default the user enter the number as decimal
        num, den = map(float, x.split('/'))
        x = str(num / den)
        return x
    else:
        return x


# Exercise 1: This function gets two strings as arguments, checks whether at least one of the strings is contained in
# the other, and returns True or False - respectively.
def substrings(str1, str2):
    answer = ((str1 in str2) or (str2 in str1))
    return answer


# Exercise 2: This function calculate the n root of the number x, and returns the answer such that
# abs(ans**n-x)<epsilon while we assume that n is a positive int

def n_root(cube, power, epsilon):
    try:
        cube = float(fraction(cube))
        power = int(power)
        epsilon = float(fraction(epsilon))
        temp2 = 0
        temp2 = temp2 + power
        if power <= 0:  # i assume that you meant that i can't get these values
            return "There is no answer for these values"
        if epsilon < 0:
            return "There is no answer for these values"
        if cube < 0 and power % 2 == 0:
            return "There is no answer for these values"
        elif cube == 0 and power == 0:  # If i supposed to get 0, if not - ignore this statement
            return "There is no answer for these values"
        elif epsilon == 0:
            return n_root2(cube, power)
        else:
            if 0 < abs(cube) < 1:
                power = 1 / power
            else:
                power = power
            ceil = abs(cube)
            floor = 0
            guess = (ceil + floor) / 2.0  # bisection
            while abs(guess ** power - abs(cube)) >= epsilon:
                if guess ** power < abs(cube):
                    floor = guess  # we'll redefine the limits
                else:
                    ceil = guess
                guess = (ceil + floor) / 2.0
            if cube < 0:  # for the negative values
                guess = -guess
            if (int(abs(cube)) - abs(cube)) == 0:
                cube = int(cube)
            if temp2 == 1:
                temp2 = f"{temp2}rd"
            elif temp2 == 2:
                temp2 = f"{temp2}nd"
            elif temp2 == 3:
                temp2 = f"{temp2}rd"
            else:
                temp2 = f"{temp2}th"
        if int(guess) - guess == 0:
            guess = int(guess)
        if int(guess) - guess == 0:
            guess = int(guess)
        return f"The closest {temp2} root of the number {cube} is: {guess}"
    except:
        print("Try again.")
        return n_root(input("Please enter a number:\n"), input("Please choose the desired root:\n"),
                      input("Please choose an epsilon:\n"))


# Second option
def n_root2(x, n):
    try:
        x = float(x)
        n = int(n)
        if x < 0 and (n % 2) == 0:
            return f"There is no answer for these values"
        if x == 0 and n == 0:
            return f"There is no answer for these values"
        if n == 0:
            return f"There is no answer for these values"
        else:
            ans = abs(x) ** (1 / n)
            if x < 1:
                ans = -ans
            if int(abs(x)) - abs(x) == 0:
                x = int(x)
            if n == 1:
                n = f"{n}rd"
            elif n == 2:
                n = f"{n}nd"
            elif n == 3:
                n = f"{n}rd"
            else:
                n = f"{n}th"
            return f"The {n} root of the number {x} is {ans}"
    except Exception as e:
        print("Try again.")
        x = input("Please choose a number:\n")
        n = input("Please choose a power:\n")
        return n_root2(x, n)


# Exercise 3: We're using the function from exercise 2 for specific epsilon and a range of 5 roots
def checkroot(x):
    # global temp3
    epsilon = 0.001
    check = True
    root = 1  # Its similar to power - root 1 of 9 = 9 root 2 9 = sqrt(9)
    ans = lambda val: n_root(str(val), str(root), str(epsilon))
    while check:
        try:
            x = float(x)
            if root > 5:
                check = False
            else:
                if x < 0 and (root % 2) == 0:  # Did this because it look better when it print it once
                    print("There is no answer for these values")
                    temp3 = -x
                    print(ans(temp3))
                else:  # Print x , -x and 1/ x if exist
                    if x != 0:
                        temp3 = x
                        print(ans(temp3))
                    if x == 0:  # I don't understand if 0 is a valid value so i did this as an optional addition
                        temp3 = 0
                        print(ans(temp3))
                    if x != 1 and x != 0:
                        temp3 = 1 / x
                        print(ans(temp3))
                    if (root % 2) != 0:
                        temp3 = -x
                        print(ans(temp3))
                root += 1
        except Exception as e:
            print("Try again. please choose a number:\n")
            return checkroot(input())


# Exercise 4:we use z as a variable that contains the value of g(x), so that it transfer the value of x, which is 3,
# to the function g(x). In the function, x = x + 1, print the line with value of x = 4, anr return the value to z.
# Here the function h is without an argument, so it doesnt affect the process, if i remove all the lines it has been
# mentioned at, i get the same result.
# also, because the function is g and the local variable in function is x, we can change the global variable to a
# different name, respectively, and the process won't change.
# Because h() is getting no local variable in the function, x returns None
# In short - we get global variables g = code, x = 3, z = 4.
# we can modify the global variables so that it will transfer
# the values and get the values by the functions

# show the changes to prove
# def h(x):
#     print(x)
#     x = x + 2
#     print(x)
#     return x
#
# def g(x):
#     x = x + 1
#     print(h(x))
#     print(x)
#     return x


# c = 3
# z = g(c)


# Exercise 5: This function gets 2 inputs, and returns their quotient and the reminder
def find(n, m):
    try:
        n = float(n)
        m = float(m)
        if n != 0 and m != 0:
            q = n // m
            r = n % m
            if int(q) - q == 0:
                q = int(q)
            if int(r) - r == 0:
                r = int(r)
            return f"The quotient is: {q}\nThe reminder is: {r}\nalso, {n} / {m} = {n / m}\n{m} / {n} = {m / n}"
        else:
            if n == 0 and m != 0:
                q = n // m
                r = n % m
                return f"The quotient is: {q}\nThe reminder is: {r}\nalso, {n} / {m} = {n / m}"
            elif m == 0 and n != 0:
                return f"The only answer is {m} / {n} = {m / n}"
            elif m == 0 and n == 0:
                return f"There is no answer for these numbers {m} / {n} - division by 0"
    except Exception as e:
        print("Wrong input. please choose only numbers:\n")
    return find(input(), input())


# Exercise 6: This function gets two numbers and returns their multiplication.
def mul_2nums(a, b):
    try:
        a = float(a)
        b = float(b)
        mul = a * b
        temp6 = mul
        if mul <= 0:  # i assume that you said that if the multiplication < = 0 than the result is 0
            temp6 = 0
        if int(temp6) - temp6 == 0:
            temp6 = int(temp6)
        return f"The multiplication {temp6}\n"
    except Exception as e:
        return mul_2nums(input("Wrong input, choose:\n"), input("\n"))


# Exercise 7: This function is getting 5 inputs, and removing every 2 steps elements
list7 = []
orig_list = []


def list_re():
    global orig_list
    for j in range(0, 5):  # I don't know if we were supposed to get only numbers. if it was the case,
        if j == 0:  # i would have change to float(input)) and int if necessary
            list7.append(input("Please enter 5 elements:\n"))
        else:
            list7.append(input())
    orig_list = orig_list + list7
    for i in range(0, 3, 2):  # i assume that for list [1, 2, 3, 4, 5] i supposed to get [2, 3, 5]
        list7.remove(list7[i])
    else:
        return f"The original list: {orig_list}\nThe transformed list   {list7}"


# Exercise 8: This function flatten the list we get (as a pre- chosen list, and not as an input), and sum the elements
# by type cases
def summer(data):
    try:
        flat_data = [y for x in data for y in (x if isinstance(x, list) else [x])]
        data = flat_data
        flat_data = sum(flat_data) if not isinstance(flat_data[0], str) else ''.join(flat_data)
        return flat_data
    except TypeError:
        return data

listsum = []
count_thelist = 0


def summer2(x): ## Function summer input
    global count_thelist, tempx
    add = True
    while add:
        if x == "done": # When to stop filling
            add = False
        else: # We're converting data type
            if x.lstrip("-").replace('.', '').isdigit():
                x = float(x)
                if x - int(x) == 0:
                    x = int(x)
                else:
                    x = float(x)
            else:
                if x == "True" or x == "False":
                    if x == "True":
                        x = True
                    else:
                        x = False
                else:
                    x = str(x)
            if x == "next list": # Switching between lists
                count_thelist += 1
                if count_thelist < linum:
                    print(f"Please enter the elements of list no.{count_thelist+1}")
                    x = summer2(input())
                else:
                    print("Out of range.")
                    summer2("done") # Sum when can't fill it
                    break
            elif x != "next list":
                listsum[count_thelist].append(x)
                x = input()
                summer2(x)
        try:
            flatten_list = [el for ind in listsum for el in (ind if isinstance(ind, list) else [ind])]
            tempx = flatten_list
            sum_x = sum(tempx) if not isinstance(tempx[0], str) else ''.join(tempx)
            x = f"The sum of the list(s) is {sum_x}"
            return x
        except Exception as e:
            x = f"The sum of the list(s) is {tempx}"
            return x

#main
print("Exercise 1:")
string1 = input("Please enter first string:\n")
string2 = input("Please enter second string:\n")
print(substrings(string1, string2))
print("\n")

print("Exercise 2:")
num_x = input("Please enter a number:\n")
num_n = input("Please choose the desired root:\n")
eps = input("Please choose an epsilon:\n")
print(n_root(num_x, num_n, eps))
print("\n")

print("Exercise 2: another option")
number2 = input("Please choose a number:\n")
powe = input("Please choose a power:\n")
print(n_root2(number2, powe))
print("\n")

print("Exercise 3:")
num3 = input("Please choose a number:\n")
checkroot(num3)
print("\n")

print("Exercise 5:")
num1 = input("Please enter two numbers:\n")
num2 = input("")
print(find(num1, num2))
print("\n")

print("Exercise 6:")
a6 = input("Please choose a number:\n")
b6 = input("The second number:\n")
print(mul_2nums(a6, b6))
print("\n")

print("Exercise 7:")
print(list_re())
print("\n")

print("Exercise 8:")
print(summer([[1, 2, 3, 'a'], [4, 'b', 'c', 'd']]))
print(summer([10, 11, 12, 0.75]))
print(summer([True, False, True, True]))
print(summer(['aa', 'bb', 'cc']))
print(summer([11, 3, 8, 9, 0.5]))
print(summer([-9, 0.1, 1]))
# # try different list, unmark
# print(summer([]))

print("Exercise 8 using input:")
linum = input("Please choose the number of lists:\n")
flag = True
while flag:
    try:
        linum = int(linum)
        flag = False
    except Exception as e:
        linum = input("Numbers as integers only:\n")

ele = input("Please enter the elements of the first list, separated by 'enter':\nTo enter the elements of"
            " the next list, enter 'next list'\nWhen done filling, and for getting sum, enter 'done':\n")
listsum = [[i for temp8 in listsum] for i in range(linum)]
print(summer2(ele))
#final edit update 12/4