######################
##  Nohar_Batit    ###
##   315572941     ###
######################

################################
# variables #
list_temp4 = []
list_temp51 = []
list_temp52 = []
list_temp53 = []
list_temp3 = []
list_temp5 = []
tuple1 = ()
tuple2 = ()
num_in_range = {}
list3_final = []
counter = 0


# Formatting input type #


def type_input(x):
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
    return x


#### Get input functions ####


def get_input1(number):
    global tuple1, tuple2, counter
    get = True
    while get:
        number = type_input(number)
        try:
            if counter == 0:
                if number == "next":  # flag end entering
                    counter += 1
                    number = input("Please enter elements of second tuple:\n")
                    return get_input1(number)
                else:
                    tuple1 = tuple1 + (number,)  # add tuples use operator
                    number = input()
                    return get_input1(number)
            if counter == 1:
                if number == "next":
                    return elements_in_common1(tuple1, tuple2)
                else:
                    tuple2 = tuple2 + (number,)
                    number = input()
                    return get_input1(number)
            return
        except Exception as e:
            number = input("Try again.\n")
            return get_input1(number)


def get_input2(number):
    get = True
    while get:
        number = type_input(number)
        try:
            number = int(number)
            b = int(input("Please enter second number:\n"))
            return gcd_lcm(number, b)
        except Exception as e:
            number = input("Try again.\n")
            return get_input2(number)


def get_input3(number):
    get = True
    while get:
        number = type_input(number)
        try:
            if number == "next":
                return no_duplicates(list_temp3)
            else:
                list_temp3.append(number)
                number = input()
                return get_input3(number)
        except Exception as e:
            number = input("Try again.\n")
            return get_input3(number)


def get_input4(number):
    get = True
    while get:
        number = type_input(number)
        try:
            if number == "next":
                try:
                    range_a = float(input("Please choose a minimum range:"))
                    range_b = float(input("Please choose a maximum range:"))
                    if range_a == int(range_a):  # check if integer
                        range_a = int(range_a)
                    if range_b == int(range_b):
                        range_b = int(range_b)
                    return count_duplicates_in_range(list_temp4, range_a, range_b)
                except Exception:
                    print("Try again. Enter numbers only")
                    return get_input4("next")  # getting only range
            else:
                if type(number) == int or type(number) == float:
                    list_temp4.append(number)
                    number = input()
                    return get_input4(number)
                else:
                    number = input("Please choose a number:\n")
                    return get_input4(number)
        except Exception as e:
            number = input("Try again.\n")
            return get_input4(number)


def get_input5(number):
    global list_temp51, list_temp52, list_temp53, list_temp5, counter
    get = True
    while get:
        number = type_input(number)
        try:
            if number == "next":
                if counter == 0:
                    list_temp51 = [] + list_temp5  # use the list_temp51 like a temp contains list_temp5
                    number = input("Please enter elements of second list:\n")
                    counter += 1
                    list_temp5 = []
                    return get_input5(number)
                elif counter == 1:
                    list_temp52 = [] + list_temp5  # done entering second list
                    number = input("Please enter elements of third list:\n")
                    counter += 1
                    list_temp5 = []
                    return get_input5(number)
                elif counter == 2:
                    list_temp53 = [] + list_temp5
                    break
            else:
                list_temp5.append(number)
                get_input5(input())
            return list(elements_in_common5_a(list_temp51, list_temp52, list_temp53))
        except Exception as e:
            number = input("Try again.\n")
            return get_input5(number)


######################

# Exercise 1: This function gets 2 tuples, and returns a "result" tuple, which it's elements are the commons.


def elements_in_common1(t1, t2):
    check1 = set(t1)
    check2 = set(t2)
    return tuple(check1 & check2)  # As tuple format


# Exercise 2: This function gets 2 integers, and returns a tuple with their lcm and gcd
# If meant without 1, than i'd return None - but for my understanding, return 1 if None.
# also, if without negative, check if a, b > 0 or if only both are negatives, check before abs a < 0 and b < 0, and
# return the values as negative
# lcm = int(a * b / gcd) If needed too
def gcd_lcm(a, b):
    try:
        a = int(a)  # Check the type
        b = int(b)  # Check the type
        gcd = 1
        a = abs(a)  # There is a comment about it above
        b = abs(b)
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                gcd = i
        smallest = gcd
        for j in range(2, a + 1):
            if ((a / j - int(a / j)) == 0) and ((b / j - int(b / j)) == 0):  # check if are integers
                smallest = j
            return smallest, gcd
    except Exception as e:
        return gcd_lcm(input("Integers only, please try again."), input())


# Exercise 3: This function gets a list, and returns the list without duplicates.


def no_duplicates(list3):
    for i in list3:
        if i not in list3_final:
            list3_final.append(i)
    list3 = list3_final
    return list3


# Exercise 4: This function gets 3 arguments - a list and a range. It returns the number of times a number,(only
# the ones in given range), appears in the list.
# Decided to return as a tuple which i explain it's meaning

def count_duplicates_in_range(list4, start, end):
    for i in list4:
        if start < i < end:
            num_in_range[i] = list4.count(i)
    return f"The number in range : The number of appears\n{num_in_range}"


# Exercise 5: This function gets 3 lists and leaves in the first one only the elements in common.


def elements_in_common5_a(list1, list2, list3):
    list1_set = set(list1)
    list1_2 = list1_set.intersection(list2)
    list1 = set(list1_2)
    list1 = list1.intersection(list3)
    return list(list1)


# Manual input #
print("**Manual input**\n")
# Exercise 1:
print("Exercise 1:")
print(elements_in_common1((1, 5, "go"), (5, 8, -1)))
counter = 0
print("")

# #Exercise 2:
print("Exercise 2:")
print(gcd_lcm(20, 40))
print("")

# Exercise 3:
print("Exercise 3:")
print(no_duplicates([3, 5, 89, "sky", 7, 5, "sky"]))
# resetting list clear for future using, please don't enter elements
list3_final = []
print("")

# Exercise 4:
print("Exercise 4:")
print(count_duplicates_in_range([2.3, 5, 9, 2.3, 4, 90, 1], 1, 5))
# clear
num_in_range = {}
print("")

# Exercise 5:
print("Exercise 5:")
print(elements_in_common5_a([1.1, -3, True, 9], [11.1, "hi", 9, -3, True, 1.1, False, -5.1], [3, "hi", 1.1, True, -3]))
counter = 0
print("")

# Input method #
print("**Using input method**\n")
# Exercise 1:
print("Exercise 1:")
print(get_input1(input("Please enter elements first tuple:\nenter next to move to next step\n")))
counter = 0
print("")

# Exercise 2:
print("Exercise 2:")
print(get_input2(input("Please enter an integer:\nPlease notice that if you enter a wrong input, you will "
                       "re-enter the numbers\n")))
print("")


# Exercise 3:
print("Exercise 3:")
print(get_input3(input("Please enter elements of the list:\nenter next to get answer\n")))
print("")

# Exercise 4:
print("Exercise 4:")
print(get_input4(input("Please enter numbers of the list:\nenter next to move to next step\n")))
print("")

# Exercise 5:
print("Exercise 5:")
print(get_input5(input("Please enter elements for first list, enter next to fill next one:\n")))
