# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:03:35 2020

@author: nati1

"""


### Q1 ###

class student(object):
    def __init__(self, name, math):
        name_condition = name.split(" ")
        assert len(name_condition) == 2, "The name you have entered is not valid"
        self.name = name
        assert type(math) == int and math <= 100 and math >= 0, "Please enter integer type as math value"
        self.math = math

    def get_name(self):
        return (self.name)

    def get_math(self):
        return self.math

    def __str__(self):
        math_grade = str(self.math)
        info = "Student info:\nName : " + self.name + "\nMath test score :" + str(math_grade)
        return (info)

    def __add__(self, s2):
        new_score = max(self.math, s2.math)
        self.math = s2.math = new_score
        if self.__class__ == eng_student and s2.__class__ != eng_student:
            phys1_grade = self.phys1
            s2 = eng_student(s2.name, s2.math, phys1_grade)
        elif s2.__class__ == eng_student and self.__class__ != eng_student:
            phys1_grade = s2.phys1
            self = eng_student(self.name, self.math, phys1_grade)

        return tuple((self.name, s2.name))


class eng_student(student):
    def __init__(self, name, math, phys1):
        student.__init__(self, name, math)
        self.phys1 = phys1


Nati = eng_student("Nati Iyov", 73, 85)
Sagi = student("Sagi Krief", 68)

Sagi + Nati
print(type(Sagi))




















