# ######################
# ##  Nohar_Batit    ###
# ##   315572941     ###
# ######################

# ################################
import random
import numpy

def f1(num1, num2, num3):
    if num1 < 0 or num2 < 0 or num3 < 0:
        return "Enter numbers higher than 0"
    res = 0
    if num1 > num2:
        temp = num2
    else:
        temp = num1
    if temp > num3:
        temp = num3
    if temp != 0:
        for i in range(1, temp+1):
            if (num1 % i == 0) and (num2 % i == 0) and (num3 % i == 0):
                res = i
    if res == 0:
        return "No such number"
    return res

# The function gets 3 integers, and casting them to positive integers - O(1) * 6
# Create a variable 0(1) * 1
# For loop range of a random variable - O(n)
# n ( (1/n) *6 + (1/n) + 1 ) , n ---> inf ; => O(n)
comp1 = "O(n)"


# Question 2
# function f2 gets 3 lists and returns a new list of elements that appear exactly in 2 lists
# (multiple answer for same numbers)
def f2(l1, l2, l3):
    result = []
    for i in l1:
        if i in l2 and i not in l3:
            result.append(i)
        elif i in l3 and i not in l2:
            result.append(i)
    for j in l2:
        if j in l3 and j not in l1:
            result.append(j)
        if j in l1 and j not in l3:
            result.append(j)
    for k in l3:
        if k in l1 and k not in l2:
            result.append(k)
        if k in l2 and k not in l1:
            result.append(k)
    return result


list1 = [1, 2, 3, 4, 9, 9]
list2 = [2, 5, 6, 1, 7, 2]
list3 = [7, 8, 9, 1, 7]
# print(list1)
# print(list2)
# print(list3)
print()
print("Question 2")
print(f2(list1, list2, list3))


# Question 3
# function f3 uses the bisection_sqrt function to find the closest 5 sqrt of the number x
def bisection_sqrt(x, eps):
    temp = abs(x)
    low = 0
    high = temp
    ans = (high+low) / 2.0
    while abs(temp - ans**5) >= (temp/eps):
        if ans**5 < temp:
            low = ans
        else:
            high = ans
        ans = (high+low) / 2.0
    return -ans


def f3(x):
    if x > -1:
        return "Enter a number smaller than -1"
    return bisection_sqrt(x, 1000000)


print()
print("Question 3")
print(f3(-2))
# Question 4


# function finds the elements in both dictionaries and returns 1 dictonary without copies of all the elements
# found in both dictionaries in the correct location
def f4(dict1, dict2):
    result_dict = {}
    for p in range(10):
        result_dict[p] = []
        for j in dict1[p]:
            temp = j
            for k in dict2[p]:
                if k == temp and k not in result_dict[p]:
                    result_dict[p].append(temp)
    return result_dict


def find(f):
    temp = abs(f)
    if temp > 10:
        return find(temp / 10)
    else:
        return temp


dictionary1 = {0: [], 1: [10, 11], 2: [], 3: [], 4: [40], 5: [5, 5], 6: [], 7: [], 8: [], 9: []}
dictionary2 = {0: [], 1: [10, 10, 11], 2: [], 3: [30], 4: [], 5: [5], 6: [], 7: [], 8: [], 9: []}
# random input into dictionaries
for key in range(10):
    dictionary1[key] = []
    dictionary2[key] = []
for val in range(5):
    num = random.randint(0, 9)
    temps = find(num)
    for i in range(10):
        if i == temps:
            dictionary1[i].append(num)
    num = random.randint(0, 10)
    temps = find(num)
    for j in range(10):
        if j == temps:
            dictionary2[j].append(num)
print("First dictonary:", dictionary1)
print("Second dictonary:", dictionary2)
print("Elements in both dictionaries:\n", f4(dictionary1, dictionary2))

class c5(object):
    def __init__(self, a):
        if a <= 0:
            raise AssertionError("The square you're creating is illegal!")
        self.a = a

    def area(self):
        """
        This function return the are aof the square.

        :return: The side length ** 2.
        """
        return self.a ** 2

    def __add__(self, other):
        new_side = (self.area() + other.area()) ** 0.5
        new_square = c5(new_side)
        return new_square

    def __str__(self):
        """
        This function print and object of square.

        :return: Detail of the square.
        """
        return f"This object is a square that the length of his side is {self.a}"


class c5b(c5):
    """
    This class represents a attributed square. An attributed square also has 1 property: side length 'a'.
    attributed square side length has to be an integer.
    """
    def __init__(self, a):
        """
        This function initialize new object of attributed square.

        :param a: The side length.
        """
        c5.__init__(self, a)
        if type(self.a) is not int:
            raise AssertionError("This attributed square side length isn't integer!")

    def __add__(self, other):
        new_side = (self.area() + other.area()) ** 0.5
        if new_side == int(new_side):
            new_attr_square = c5b(int(new_side))
            return new_attr_square
        else:
            new_square = c5(new_side)
            return new_square

    def __str__(self):
        """
        This function print and object of attributed square.

        :return: Detail of the attributed square.
        """
        return f"This object is a attributed square that the length of his side is {self.a}"


# ----------------------------------------------------------------------------------------------------------------------
#Flipping a coin 'n' times. The goal is to evaluate the probability of getting exactly 1/2 of the times heads

print("\nQuestion No.6:")


def f6(n):
    random.seed(1)
    total = 0
    for i in range(10 ** 4):
        result = []
        for j in range(n):
            result.append(random.choice([0, 1]))
        if result.count(0) == (n / 2):
            total += 1
    EP = total / (10 ** 4)
    return EP



def f7a(list_of_tuples):
    """
        This function receive features and calibrate it according to the z-scaling method.
        """
    def z_scaling(features):
        mean_value = numpy.mean(features)
        sd = numpy.std(features)
        for j in range(len(features)):
            features[j] = features[j] - mean_value
            features[j] = features[j] / sd
        return features

    st_grade, st_works = [], []
    for i in range(len(list_of_tuples)):
        st_grade.append(list_of_tuples[i][1])
        st_works.append(list_of_tuples[i][2])
    st_grade = z_scaling(st_grade)
    st_works = z_scaling(st_works)
    list_of_students = []
    for k in range(len(list_of_tuples)):
        if len(list_of_tuples[k]) == 3:
            new_student_db = [list_of_tuples[k][0], st_grade[k], st_works[k]]
            list_of_students.append(new_student_db)
        else:
            new_student_db = [list_of_tuples[k][0], st_grade[k], st_works[k], list_of_tuples[k][3]]
            list_of_students.append(new_student_db)
    return list_of_students

def f7b(t, L):
    """
    This function receive student 't' and list of students 'L' . This function return 3 student from 'L' that are
    the closest to 't' (oclade distance).
    """
    """
    This function return the oclade distance between 2 vectors.

    :param student_t: The first student.
    :param student_other: The other student.
    :return: distance ** (1 / 2) - The oclade distance between 2 vectors.
    """
    def oclade_dist(student_t, student_other):
        distance = 0
        for i in range(1, 3):
            distance += abs(student_t[i] - student_other[i]) ** 2
        return distance ** (1 / 2)

    k_nearest, distances = [], []
    for j in range(3):
        k_nearest.append(L[j])
        distances.append(oclade_dist(t, L[j]))
    max_dist = max(distances)
    for e in L[3:]:
        dist = oclade_dist(t, e)
        if dist < max_dist:
            max_index = distances.index(max_dist)
            k_nearest[max_index] = e
            distances[max_index] = dist
            max_dist = max(distances)
    return k_nearest

def f7c(t, L):
    close_students = f7b(t, L)
    labels = []
    for i in range(len(close_students)):
        labels.append(close_students[i][3])
    if labels.count(0) > labels.count(1):
        t.append(0)
    else:
        t.append(1)
    return t

# Question 8
# f8 function is a recursive function finding the n!! = n(n-2)(n-4)(n-6)...[(1) or (2)]
# depending of n number
def f8(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n * f8(n - 2)




print()
print("Question 8")
print(f8(4))
comp8 = "O(n)"
print("Complexity of the code is:", comp8)
# complexity is O(n) because f8 is a recursive function that does the recursion n times (depends on the n given)




