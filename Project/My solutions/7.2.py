class Error(Exception):  # Errors
    pass


class NotAnInput(Error):
    pass


class NoneFound(Error):
    pass


class AssertionError1(Error):
    pass


class AssertionError2(Error):
    pass


def print_3():  # Print menu 3 function
    print("1.Add an simple alien")
    print("2.Add an super alien")
    print("3.Change a name")
    print("4.Change a color simple")
    print("5.Print the alien simple")
    print("6.Change a color super")
    print("7.Print the alien super")
    print("8.Combine the aliens (can do simple+super)")
    print("9.Combine the aliens (can't fo simple+super)")
    print("10.Print menu")
    print("11.Exit")


alien_dict = {}
super_alien_dict = {}


def print_alien_simple():  # Print the aliens as tuples
    for k in alien_dict.items():
        print(k)


def print_alien_super():
    for i in super_alien_dict.items():
        print(i)


list_aliens = []
color_comb = dict(red={"yellow", "blue"}, yellow={"red", "blue"}, blue={"yellow", "red"})

class Alien:  # Class with own attributes. use it to create new objects

    def __init__(self, name, color, title=None):  # Constructor
        self.name = name
        self.color = color
        global color_comb
        self.name_combined = ""
        self.color_combined = ""
        self.color_comb = ""
        self.check_color()
        self.title = title


    def __str__(self):
        return f"alien:{self.name}:{self.color}"


    def check_color(self):  # Check colors using dictionary
        if self.color in color_comb.keys():
            pass
        else:
            raise AssertionError1("AssertionError: This is not an alien data")

    def __add__(self, other):
        if self.title == other.title:
            if self.title is None:
                return f"alien:{self.set_combined_alien_name(other)}:{self.set_combined_alien_color(other)}"
            else:
                return f"alien:{self.set_combined_alien_name(other)}:{self.set_combined_alien_color(other)}:{self.title}"
        return f"alien:{self.set_combined_alien_name(other)}:{self.set_combined_alien_color(other)}:{self.title}"

    def add2(self, other):
        if isinstance(self, Alien) or isinstance(other, Alien):
            raise AssertionError
        else:
            if self.color is None:
                return f"alien:{self.set_combined_alien_name(other)}:{self.set_combined_alien_color(other)}"
            else:
                return f"alien:{self.set_combined_alien_name(other)}:{self.set_combined_alien_color(other)}:{self.title}"


    def set_combined_alien_color(self, other):
        self.color_combined = {self.color, other.color}
        if self.color_combined == color_comb["red"]:  # Specified combination check
            self.color_combined = "red"
        elif self.color_combined == color_comb["yellow"]:
            self.color_combined = "yellow"
        elif self.color_combined == color_comb["blue"]:
            self.color_combined = "blue"
        else:
            self.color_combined = self.color
        return self.color_combined

    def set_combined_alien_name(self, other):
        if (len(self.name) != 2) or (len(other.name) != 2):
            raise AssertionError
        else:
            self.name_combined = self.name[0] + other.name[0]
        return self.name_combined



class SuperAlien(Alien):
    def __init__(self, name, color, title='Lord'):
        super().__init__(name, color, title)
        self.title = title


    def __str__(self):
        return f"alien:{self.name}:{self.color}:{self.title}"



def menu3():
    try:
        a = SuperAlien("ab", "blue")
        b = SuperAlien("dd", "blue")
        c = Alien("ed", "blue")
        print(a)
        print(a+b)
        print(a+c)
        print(a.add2(c))  # second case
    except AssertionError:
        return 'AssertionError'