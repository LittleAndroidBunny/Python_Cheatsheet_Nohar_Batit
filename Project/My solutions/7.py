import sys
import Nohar_Batit3
import Nohar_Batit4
import Nohar_Batit5
import Nohar_Batit2
class Error(Exception):  # Errors
    pass

class Start(Error):  # Use to print the main
    pass

class NotAnInput(Error):
    pass

class NoneFound(Error):
    pass


def print_menu():  # menu of class
    print("menu")
    print("Please choose a class:")
    print("1.)  Gym - print example object")
    print("2.) Trainers")
    print("3.) Subscribers")
    print("4.) Exit")


if __name__ == '__main__':
    ans = Nohar_Batit2.menu3()  # class Alien please check file Nohar_Batit2
    if ans == 'AssertionError':
        print('AssertionError')  # so you could continue
    print("Please check file nohar_batit6 for the big o functions")
    go = True
    while go:
        try:
            print_menu()  # Main menu of class
            question = int(input())
            if question == 1:
                ans = Nohar_Batit3.Gym('nohar batit', 'F', 'Fitness club', '9/1/1998', 'T')
                print(ans.information())
                if ans == 1:
                    raise Start
            elif question == 2:
                ans = Nohar_Batit4.run2()
                if ans == 1:
                    raise Start
                elif ans == 0:
                    sys.exit()
            elif question == 3:
                ans = Nohar_Batit5.run3()
                if ans == 1:
                    raise Start
                elif ans == 0:
                    sys.exit()
            elif question == 4:  # exit code
                print("Thank you!")
                sys.exit()
        except ValueError:
            print("Wrong choice. Try again")
        except Start:
            loop = True
