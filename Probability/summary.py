# # -*- coding: utf-8 -*-
# """
# Created on Fri Jun  5 00:34:43 2020
#
# @author: nati1
# """
#
#
# ## Modules
# import mymodule
# mymodule.greeting(Nati)
#
# import mymodule as package
# a = package.greeting(Nati)
#
#
# from mymodule import person1
# print(person1["age"])
#
#
# # dir(mymodule) - gives all the func/list - basically all the properties that the imported module has
#
# # random.seed(int) - בהפעלה ראשונה מתקבל ערך רנדומלי, לאחר מכן בכל הפעלה של הפונקצייה יתקבל אותו ערך שהתקבל
# רנדומלית בהתחלה
#
# DATA TYPES:
#     Numerical - limited to integers
#     Categoric - cant distinct between categories. Example : blue vs white - whos to say whats better ?
#     Ordinal - objects that are not int type but can be measured with one another. Example :
#         student grades A vs B - we know whats "better" (A).
#
#         Mean - simple average Value
#         Median - mid point Value
#         Mode - The most common Value
#
# commonly used packages: numpy - includes median package (numpy.median(list)) , includes std (standart deviation)
# package - numpy.std(list) scipy - includes mode package  (scipy.mode(list))
#
#
#
# Varience :
# Varience = std''s squared sum divided by number of objects
# V = (std1^2 + std2^2 + std3^2 + ... stdn^2) / n
#
# Total standart deviation - sqrt(V)
#
#       ### std sidenote:
#           most of the values will usually be inside [M-std,M+std] but its not obligating !!!
#
#
#
#
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
#
# What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
#
# The NumPy module has a method for finding the specified percentile:
#
# Example
# Use the NumPy percentile() method to find the percentiles:
#
# import numpy
#
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
#
# x = numpy.percentile(ages, 75)
#
#
#
# *** How to create a list of as many random floats (!!) between certain values :
#     numpy.random.uniform (low , high ,number of times)
#
#
# import numpy
# import matplotlib.pyplot as plt
#
# x = numpy.random.uniform(0.0, 5.0, 250)
#
# plt.hist(x, 5)
# plt.show()
#
#
#
# Data representation as scattered dots :
#
#
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#
# plt.scatter(x, y)
# plt.show()
#
#
#
# usful plot functions :
# import matplotlib.pyplot
#
# plt.plot (l1,l2)
# plt.hist(list,bins)
# plt.scatter(l1,l2)
#
#
#
