# ######################
# ##  Nohar_Batit    ###
# ##   315572941     ###
# ######################
#
# ################################

import numpy


#### Euclidean distance :


def oaklidian_distance(i, j):
    prop16_dis = p16[i] - p16[j]
    prop17_dis = p17[i] - p17[j]
    return ((prop16_dis) ** 2 + (prop17_dis) ** 2) ** 0.5


def euklidian2(student1, student2):
    dv = p18[student1] - p18[student2]
    di = p21[student1] - p21[student2]
    distance = ((dv) ** 2 + (di) ** 2) ** 0.5
    return distance


def euklidian3(student1, student2):  #finding the Euclid distance(Pythagorean distance)
    dv = p14[student1] - p14[student2]
    di = p25[student1] - p25[student2]
    distance = ((dv) ** 2 + (di) ** 2) ** 0.5
    return distance




#### 16th and 17th properties go 1/0 and appending the 32(Final Grade) :

f = open("Data1.txt")
p16 = []
p17 = []
p32 = []
for i in f: #we switch the yes and no to 1 and 0 into new lists
    individual = i.split(";")
    if individual[15] == '""yes""':
        p16.append(1)
    elif individual[15] == '""no""':
        p16.append(0)
    p32.append(individual[32])

    if individual[16] == '""yes""':
        p17.append(1)
    elif individual[16] == '""no""':
        p17.append(0)

### Final Grades list by integers :

FG = []
FG1 = []
for e in p32:
    e = e.split('"\n')
    FG1.append(e)

for i in FG1:
    FG.append(int(i[0]))

bigger = []
smaller = []
combined = []

for i in range(len(FG)):
    for n in range(len(FG)):
        if i > n:
            if FG[i] > 10 and FG[n] > 10:
                bigger.append(oaklidian_distance(i, n))
            elif FG[i] <= 10 and FG[n] <= 10:
                smaller.append(oaklidian_distance(i, n))
            else:
                combined.append(oaklidian_distance(i, n))

bigger_avg = numpy.mean(bigger)
smaller_avg = numpy.mean(smaller)
combined_avg = numpy.mean(combined)
print(bigger_avg, smaller_avg, combined_avg)

#### Properties 18 and 21 :
#parameters of 18 and 21
# we do the question 1-4 for 5 as well
# the avg is a bit lower than previous question
F = open("Data1.txt")
p18 = []
p21 = []
p33 = []
for i in F:
    individual = i.split(";")
    final_grade = individual[32]
    p33.append(int(final_grade.strip('"\n"')))
    if individual[17] == '""yes""':
        p18.append(1)
    else:
        p18.append(0)

    if individual[20] == '""yes""':
        p21.append(1)
    else:
        p21.append(0)

bigger = []
smaller = []
combined = []

for i in range(len(p33)):
    for n in range(len(p33)):
        if n > i:
            if p33[i] > 10 and p33[n] > 10:
                bigger.append(euklidian2(i, n))

            elif p33[i] <= 10 and p33[n] <= 10:
                smaller.append(euklidian2(i, n))

            else:
                combined.append(euklidian2(i, n))

bigger_avg = numpy.mean(bigger)
smaller_avg = numpy.mean(smaller)
combined_avg = numpy.mean(combined)

print(bigger_avg, smaller_avg, combined_avg)

"""

"""

##### Properties 14 and 24 :


f = open("Data1.txt")
p14 = []
p25 = []
p33 = []

##### Property 14 : gets 0 for 1,2 / gets 1 for 3,4
##### Property 24 : gets 0 for 1,2,3 / gets 1 for 4,5

for i in f:
    individual = i.split(";")
    final_grade = individual[32]
    p33.append(int(final_grade.strip('"\n')))
    if int(individual[13]) <= 2:
        p14.append(0)
    else:
        p14.append(1)

    if int(individual[24]) <= 3:
        p25.append(0)
    else:
        p25.append(1)

bigger = []
smaller = []
combined = []

for i in range(len(p33)):
    for n in range(len(p33)):
        if n > i:
            if p33[i] > 10 and p33[n] > 10:
                bigger.append(euklidian3(i, n))

            elif p33[i] <= 10 and p33[n] <= 10:
                smaller.append(euklidian3(i, n))

            else:
                combined.append(euklidian3(i, n))

bigger_avg = numpy.mean(bigger)
smaller_avg = numpy.mean(smaller)
combined_avg = numpy.mean(combined)


### prop 26 and 27 :


def euklidian4(student1, student2):
    dv = p26[student1] - p26[student2]
    di = p27[student1] - p27[student2]
    distance = ((dv) ** 2 + (di) ** 2) ** 0.5
    return distance


f = open("Data1.txt")
p26 = []
p27 = []
p33 = []

##### Property 26 : gets 0 for 1,2,3 / gets 1 for 3,4
##### Property 27 : gets 0 for 1,2,3 / gets 1 for 4,5

for i in f:
    individual = i.split(";")
    final_grade = individual[32]
    p33.append(int(final_grade.strip('"\n')))
    if int(individual[25]) <= 3:
        p26.append(0)
    else:
        p26.append(1)

    if int(individual[26]) <= 3:
        p27.append(0)
    else:
        p27.append(1)

bigger = []
smaller = []
combined = []

for i in range(len(p33)):
    for n in range(len(p33)):
        if n > i:
            if p33[i] > 10 and p33[n] > 10:
                bigger.append(euklidian4(i, n))

            elif p33[i] <= 10 and p33[n] <= 10:
                smaller.append(euklidian4(i, n))

            else:
                combined.append(euklidian4(i, n))

bigger_avg = numpy.mean(bigger)
smaller_avg = numpy.mean(smaller)
combined_avg = numpy.mean(combined)


# Question 4
    # find the average of the lists
    # we can learn that the Euclid distance for pair of students that has a grade greater than 10 is constant 0.0 or 1.0
    # for pair of the grade 10 or less is 0.0, 1.0 or 1.41
    # and we find the avg for the attributes 16,17  in file.txt
    # the avg of student pair getting 10 or lower is the highest


# import numpy as np
#
# # Question 1: #Get the boolean value of yes as 1 and no as 0
#
#
#
#
# list_16 = []
# list_17 = []
# main_dict = {}
# counter = 0
# # we remember we start from index 0
# file = 'Data1.txt'
# with open(file) as f:
#     main_list = [i.strip().replace('"', '').split(';') for i in f.readlines()]
# for i in main_list:
#     for j in range(len(i)):
#         if i[j].lstrip("-").replace('.', '').isdigit():
#             i[j] = float(i[j])
#             if i[j] - int(i[j]) == 0:
#                 i[j] = int(i[j])
# for i in main_list:
#     main_dict[counter] = i
#     counter += 1
# # with open(file) as f:
# #     for i in f.readlines():
# #         main_dict[counter] = i.strip().replace('"', '').split(';')
# #         counter += 1
# #
# # for i in main_dict.keys():
# #     for j in main_dict[i]:
# #         if j.lstrip("-").replace('.', '').isdigit():
# #             j = float(j)
# #             if j - int(j) == 0:
# #                 j = int(j)
# print(main_list)
# print(main_dict)
#     # main_list = [i.lstrip("-").replace('.', '').isdigit() if i[j] else str(i) for i, j in main_list]
# for i in main_dict:
#     if main_dict[i][15] == 'yes':
#         list_16.append(1)
#     else:
#         list_16.append(0)
#     if main_dict[i][16] == 'yes':
#         list_17.append(1)
#     else:
#         list_17.append(0)
#
# print("Question 1")
#
#
# print(list_16)
# print(list_17)
#
# # Question 2:
#
#
# def distance(i, j):
#     d = ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** (1 / 2)
#     return d
#
#
# print()
# print("Question 2")
# print(distance(list_16, list_17))
# # Question 3
#
# list_of_lists = []
#
# def work_with_dict(list1, list2, quest):
#     dict_of_grades = {}
#     counter = 0
#     list_bigger_than_10 = []
#     list_both_10_or_less = []
#     list_distance = []
#
#     # for i in main_list:
#     #     if i[-1] > 10:
#     #         dict_of_grades[counter] = i[-1]
#     #     else:
#     #         dict_of_grades[counter] = i[-1]
#     #     counter += 1
#     #     if quest < 6:
#     #         for l in dict_of_grades:
#     #             for j in range(l + 1, len(dict_of_grades)):
#     #                 if dict_of_grades[l] > 10 and dict_of_grades[j] > 10:
#     #                     list_bigger_than_10.append(distance((list1[l], list2[l]), (list1[j], list2[j])))
#     #                 elif dict_of_grades[l] <= 10 and dict_of_grades[j] <= 10:
#     #                     list_both_10_or_less.append(distance((list1[l], list2[l]), (list1[j], list2[j])))
#     #                 else:
#     #                     list_distance.append(distance((list1[l], list2[l]), (list1[j], list2[j])))
#     #     else:  # for question 6 when numeric and not a boolean
#     #         for l in dict_of_grades:
#     #             for j in range(l + 1, len(dict_of_grades)):
#     #                 if dict_of_grades[l] > 10 and dict_of_grades[j] > 10:
#     #                     list_bigger_than_10.append(normal((list1[l], list2[l]), (list1[j], list2[j])))
#     #                 elif dict_of_grades[l] <= 10 and dict_of_grades[j] <= 10:
#     #                     list_both_10_or_less.append(normal((list1[l], list2[l]), (list1[j], list2[j])))
#     #                 else:
#     #                     list_distance.append(normal((list1[l], list2[l]), (list1[j], list2[j])))
#         # Question 4
#     print()
#     print(f"The average of the first list: {np.average(np.real(list_bigger_than_10))}")
#     print(f"The average of the second list: {np.average(np.real(list_both_10_or_less))}")
#     print(f"The average of the third list: {np.average(np.real(list_distance))}")
#
#
# print()
# print("Question 3 + 4")
# work_with_dict(list_16, list_17, 4)
#
#
# # Question 5
# # file = open("Data1.txt")
# list_18 = []
# list21 = []
#
# # for i in file:
# #     main_list = i.split(";")
# if main_dict[i][17] == 'yes':
#     list_18.append(1)
# else:
#     list_18.append(0)
# if main_dict[i][20] == 'yes':
#     list21.append(1)
# else:
#     list21.append(0)
#
# i = 0
# print()
# print("Question 5")
# work_with_dict(list_18, list21, 5)
# i = 0
#
# # Question 6
# # Defining a func of calculating a euclidean distance of two vectors and normalizing them:
#
#
# def normal(c, k):
#     # Calculating the normals:
#     c_norma = (c[0] ** 2 + c[1] ** 2) ** (1 / 2)
#     k_norma = (k[0] ** 2 + k[1] ** 2) ** (1 / 2)
#     # Normalized vectors:
#     new_v1 = (c[0] / c_norma, c[1] / c_norma)
#     new_v2 = (k[0] / k_norma, k[1] / k_norma)
#     return ((new_v1[0] - new_v2[0]) ** 2 + (new_v1[1] - new_v2[1]) ** 2) ** (1 / 2)
#
#
# list_14 = []
# list_25 = []
#
# # file = open("Data1.txt")
#
# # for i in file:
# #     main_list = i.split(";")
#
# list_14.append(main_dict[i][13])
# list_25.append([i][24])
# print()
# print("Question 6")
# work_with_dict(list_14, list_25, 6)
#
# # Question 7
# # i chose 25 freetime and 26 goout for the last 2 parameters that i think are important
# list_26 = []
# # file = open("Data1.txt")
#
# # for i in file:
# #     main_list = i.split(";")
# list_26.append(main_dict[i][25])
# print()
# print("Question 7")
# work_with_dict(list_25, list_26, 6)
#
