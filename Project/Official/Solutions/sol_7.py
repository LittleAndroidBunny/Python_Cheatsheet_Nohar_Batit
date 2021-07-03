# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:22:41 2020

@author: nati1
"""


class Alien():
    def __init__(self, Name, Color):
        assert len(Name) == 2, "This is not an alien data"
        self.name = Name
        assert (
                    Color == "Yellow" or Color == "yellow" or Color == "Blue" or Color == "blue" or Color == "Red" or Color == "red"), "This is not an alien data"
        self.color = Color

    def __str__(self):
        info = ("Alien:" + self.name + ":" + self.color)
        return info

    def __add__(self, a2):
        assert type(self) == type(a2), "Cannot merge different status aliens"
        new_name = (self.name[0] + a2.name[1])
        new_color = "Red"
        if type(a2) == Alien:
            New = Alien(new_name, new_color)
        else:
            New = SuperAlien(new_name, new_color)

        return New


class SuperAlien(Alien):
    def __init__(self, Name, color):
        Alien.__init__(self, Name, color)
        self.status = "Lord"

    def __str__(self):
        info = ("Alien:" + self.name + ":" + self.color + ":Lord")
        return info


A1 = SuperAlien("Na", "Yellow")
A2 = SuperAlien("ad", "blue")
A3 = A1 + A2
print(A3)














