class Error(Exception):  # Errors
    pass


class NotAnInput(Error):
    pass


class NoneFound(Error):
    pass


color_comb = {"red": {"yellow", "blue"},  # I use it to get the allowed and their product
              "yellow": {"red", "blue"},
              "blue": {"yellow", "red"}}


def print_3():  # Print menu 3 function
    print("1.Add an alien")
    print("2.Change a name")
    print("3.Change a color")
    print("4.Print the alien")
    print("5.Combine the aliens")
    print("6.Print menu")
    print("7.Exit")


alien_dict = {}


def print_alien():  # Print the aliens as tuples
    for k in alien_dict.items():
        print(k)


list_aliens = []


class Alien:  # Class with own attributes. use it to create new objects
    global color_comb

    def __init__(self, name, color):  # Constructor
        self.name = name
        self.color = color
        Alien.check_color(self)

    def check_color(self):  # Check colors using dictionary
        if self.color in color_comb.keys():
            pass
        else:
            raise AssertionError("AssertionError: This is not an alien data")

    def get_alien_name(self):  # Get names
        return self.name

    def get_alien_color(self):  # Get colors
        return self.color

    def __add__(self, other):  # Combine methode
        return self.get_combined_alien(other)

    def set_combined_alien_color(self, other):  # Combine their colors
        color_combined = {self.color, other.color}
        if color_combined == color_comb["red"]:  # Specified combination check
            color_combined = "red"
        elif color_combined == color_comb["yellow"]:
            color_combined = "yellow"
        elif color_combined == color_comb["blue"]:
            color_combined = "blue"
        else:
            color_combined = self.color
        return color_combined

    def set_combined_alien_name(self, other):  # Combine their names
        name_combined = self.name[:1] + other.name[:1]
        return name_combined


    def get_combined_alien(self, other):  # Return in a more private way than add, option 2
        return f"alien:{Alien.set_combined_alien_name(self, other)}:{Alien.set_combined_alien_color(self, other)}"


    def __repr__(self):  # Methode to return as allowed
        return f"alien:{Alien.get_alien_name(self)}:{Alien.get_alien_color(self)}"


def menu3():  # This function acts as a main program of question 3
    go = True
    while go:
        try:
            print_3()
            ans = int(input("What would you like to do?\n"))  # options
            if ans == 1:
                go = False
                name = input("Choose a name:")
                alien_dict[name] = input("Choose a color:")
                go = True
            elif ans == 2:
                if not alien_dict:
                    raise NoneFound
                else:
                    print_alien()
                    name = input("Choose the name of alien you want to change:")
                    if name in alien_dict:
                        alien_dict[input("Choose the new name:")] = alien_dict[name]
                        del alien_dict[name]
                    else:
                        raise NoneFound
            elif ans == 3:
                if not alien_dict:  # Check if empty
                    raise NoneFound
                else:
                    print_alien()
                    name = input("Choose the name of alien you want to change:")
                    if name in alien_dict:
                        alien_dict[name] = input("Please enter the new color:")
                    else:
                        raise NoneFound
            elif ans == 4:
                if not alien_dict:
                    raise NoneFound
                else:
                    print_alien()
                    name = input("Please choose the name from the above aliens:")
                    color = alien_dict[name]
                    if name in alien_dict:
                        cutie = Alien(name, color)  # Create an object
                        print(cutie)
                    else:
                        raise NoneFound
            elif ans == 5:
                if not alien_dict:
                    raise NoneFound
                else:
                    print("Choose the name of aliens to combine:")
                    print_alien()
                    name1 = input("Alien 1:")  # Get from user
                    name2 = input("Aline 2:")
                    if name1 in alien_dict:
                        if name2 in alien_dict:
                            color1 = alien_dict[name1]  # Get from dictionary
                            color2 = alien_dict[name2]
                            a1 = Alien(name1, color1)
                            a2 = Alien(name2, color2)
                            print(Alien.get_combined_alien(a1, a2))  # Option one
                            print(a1+a2)  # Option two
                            print()
                        else:
                            raise NoneFound
                    else:
                        raise NoneFound
            elif ans == 6:
                return 1
            elif ans == 7:
                print("Thank you!")
                return 0
            else:
                raise NotAnInput
        except NoneFound:
            print("No alien found.")
        except NotAnInput:
            print("Wrong choice. Try again")
        except NameError:
            print("No length found. Try again")
        except ValueError:
            print("Wrong choice. Try again")
        except AssertionError:
            print("AssertionError: This is not an alien data")
            go = True



