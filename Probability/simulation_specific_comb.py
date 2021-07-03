# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:28:50 2020

@author: nati1
"""
import random


def RollDie():
    a = random.randint(1, 6)
    return a


def Test(combination, times):
    appear = 0
    for n in range(times):
        string = ''
        for i in range(len(combination)):
            randomnum = str(random.randint(1, 6))
            string = string + randomnum

        if string == combination:
            appear += 1
    chance = (1 / 6 ** len(combination))
    print("Actual probability is", round(chance, 8))
    print("Our probability is :", appear / times)


Test("11111", 10000)



