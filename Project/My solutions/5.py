# ######################
# ##  Nohar_Batit    ###
# ##   315572941     ###
# ######################
#
# ################################
class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
#I don't know if we allowed to use class already, but if not i can erase these lines,
#it 's just for more aesthetic printing, i tried to play with classes for a bit to understand how it works.


question_count = 1
lst4 = []
fibonacci_cache = {}
dict5 = {}
list6 = []


def fibonacci(n):
    if n in fibonacci_cache:  # I store the numbers for shorter running time
        return fibonacci_cache[n]
    if n == 0:  # First stop condition
        return 0
    if 0 < n <= 2:  # Second stop condition
        return 1
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2) + 2 * fibonacci(n - 3)
    fibonacci_cache[n] = value
    return value


def gcd(a, b):
    if a == b:
        return a
    if a == 0:  # Definition by wiki to gcd of zero and non-zero
        return b
    if b == 0:
        return a
    else:
        if a % 2 == 0:
            if b % 2 == 0:  # If both are even
                return 2 * gcd(a / 2, b / 2)
            return gcd(a / 2, b)  # If b odd
        else:
            if b % 2 == 0:  # If b odd
                return gcd(a, b / 2)
            else:  # If both are odd
                if a > b:  # Reduce their distance from each-other
                    return gcd((a - b) / 2, b)
                else:
                    return gcd(a, (b - a) / 2)


def power(a, b):
    if b == 0:
        if a != 0:
            return 1
        else:
            return "Illegal operation."
    else:
        if b == 1:
            return a
        else:
            return a * power(a, b - 1)


def sum_list(arr, r):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_list(arr[1:r + 1], r - 1)


# This function gets a range as an input from the user, and printing the index's value
# by calling the Fibonacci function
def question1():
    try:
        ele = int(input("Please choose a number:\n"))
        for i in range(ele):
            print(fibonacci(i), end=',')
        print(fibonacci(ele))
    except Exception as e:
        print("Numbers only.")
        return question1()


# This function gets two number as an inputs from the user, and printing their gcd by calling gcd()
def question2():
    try:
        value1 = int(input("please enter two numbers separated by enter:\n"))
        value2 = int(input())
        print(f"The gcd of {value1} and {value2} is: {int(gcd(abs(value1), abs(value2)))}")
    except Exception as e:
        print("Numbers only.")
        return question2()

#This function returns the nth power of a number that are both given by the user.
def question3():
    go = True
    while go:
        try:
            number = int(input("Please enter a number:\n"))
            if number < 0:
                raise ValueTooSmallError
            in_the_power = int(input("Please enter a power:\n"))
            answer = power(number, abs(in_the_power))
            go = False
            if (number == 0) and (in_the_power == 0):
                print(answer)
            else:
                if in_the_power < 0:
                    print(f"The answer is: {number} ** {in_the_power} = {1 / answer}")
                else:
                    print(f"The answer is: {number} ** {in_the_power} = {answer}")
        except ValueTooSmallError:
            print("Positive integer only.")
        except:
            print("Input as requested only.")


# This function sums up the values in the range that are both given by the user
def question4():
    go = True
    while go:
        try:
            global len_list
            n = int(input("Please enter the number of elements you want to enter your list:\n"))
            print("Please enter elements:")
            for i in range(n):
                element = int(input())
                lst4.append(element)  # Add the elements
            while go:
                len_list = int(input("Please choose the length of the list you want to sum:\n"))
                if len_list <= len(lst4):
                    go = False
            go = False
            print(f"The list you entered: {lst4}")
            print(f"The sum of your list: {sum_list(lst4, len_list)}")
        except:
            print("Wrong input.")
            lst4.clear()


# This function is getting a string from the user, and insert the words to a dictionary by their first character.
# The function send them to the right letter by their ascii value using chr, and save the length that every key
# (it contains)
def dictionary():
    letter = 97
    string = input("Please enter a string:\n").replace(',', " ")
    for i in range(letter, letter + 26):
        dict5.setdefault(chr(i), [t for t in string.split() if t.startswith(chr(i))])
        len_dict = len(dict5[chr(i)])
        list6.append((chr(i), len_dict))



# #Question 1:
print(f"Question {question_count}:")
question_count += 1
question1()

# # Question 2:
print(f"Question {question_count}:")
question_count += 1
question2()

# Question 3:
print(f"Question {question_count}:")
question_count += 1
question3()

# # Question 4:
print(f"Question {question_count}:")
question_count += 1
question4()

# # Question 5:
print(f"Question {question_count}:")
question_count += 1
dictionary()
print(dict5)

# # Question 6:
print(f"Question {question_count}:")
question_count += 1
print(list6)

# I combined Question 5 and 6. Assuming that's what you meant, but if not, i could
# duplicate the function to get a new input.
