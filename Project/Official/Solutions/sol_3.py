# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:52:30 2020

@author: nati1
"""
"""

### Woksheet 3 : 

### Q1 ### :

def WordInWord (w1,w2) : 
    if w1 in w2 or w2 in w1: 
        return True
    else : 
        return False 

print(WordInWord("time","times"))

"""


##### Q2 #### :

def bisection(x, n, epsilon):
    if x > 1:
        low = 0
        high = x
        ans = (high + low) / 2
        while abs(x - ans ** n) > epsilon:
            if ans ** n > x:
                high = ans
            elif ans ** n < x:
                low = ans
            ans = (high + low) / 2
        return (ans)

    if x > 0 and x < 1:
        low = 0
        high = 1
        ans = (high + low) / 2
        while abs(x - ans ** n) > epsilon:
            if ans ** n < x:
                low = ans
            elif ans ** n > x:
                high = ans
            ans = (high + low) / 2
        return (ans)

    if x < 0 and n % 2 == 1:
        high = 0
        low = x
        ans = (high + low) / 2
        while abs(x - ans ** n) > epsilon:
            if ans ** n < x:
                low = ans
            elif ans ** n > x:
                high = ans
            ans = (high + low) / 2
        return (ans)


### Q3 ### :

def Q2_Samples(x, n):
    epsilon = 0.001
    for i in range(1, 6):
        print(bisection(x, i, epsilon))
        print(bisection(1 / x, i, epsilon))
        print(bisection(-x, i, epsilon))








