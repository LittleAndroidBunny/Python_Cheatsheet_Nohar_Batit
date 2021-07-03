from math import sqrt
class Error(Exception):  # Errors
    pass

class Start(Error):
    pass

class NotAnInput(Error):
    pass

class NoneFound(Error):
    pass


def print_2():  # Print menu two
    print("1.Add length")
    print("2.Print equilateral")
    print("3.Print area")
    print("4.Print circumference")
    print("5.Print menu")
    print("6.Exit")

class Equilateral:  # Class with own attributes to create new objects
    def __init__(self, length):
        self.length = length  # Get the length

    def circumference(self):
        return self.length * 3  # Get by triangle function of circumference

    def area(self):
        return ((self.length ** 2) * sqrt(3)) / 4   # a^2 * sqrt(3) / 4

    def get_equilateral_area(self):
        return 'The area of the equilateral is: {}'.format(Equilateral.area(self))  # Return area desired

    def get_equilateral_circumference(self):  # Return circumference value
        return 'The circumference of the equilateral is: {}'.format(Equilateral.circumference(self))

    def __repr__(self):  # Methode to desired print type
        return 'T<{}>'.format(self.length)

def menu2():  # Function acs as main program of question 2
    values = 0
    go = True
    while go:
        try:
            print_2()
            ans = int(input("What would you like to do?\n"))  # Options
            if ans == 1:
                go = False
                param = int(input("Please enter the value:\n"))
                if (type(param) != int) or (param <= 0):  # Check the length
                    raise NoneFound
                else:
                    values = Equilateral(param)
                go = True
            elif ans == 2:
                print(Equilateral(param))  # Print using class
            elif ans == 3:
                if param < 0:
                    raise NoneFound
                else:
                    print(values.get_equilateral_area())
            elif ans == 4:
                if param < 0:
                    raise NoneFound
                else:
                    print(values.get_equilateral_circumference())
            elif ans == 5:
                return 1
            elif ans == 6:
                print("Thank you!")
                return 0
            else:
                raise NotAnInput
        except NoneFound:
            print("Wrong input. Try again")
            go = True
        except NotAnInput:
            print("Wrong choice. Try again")
        except NameError:
            print("No length found. Try again")
        except:
            print("Positive integers only. Try again")
            go = True
