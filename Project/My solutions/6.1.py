# ######################
# ##  Nohar_Batit    ###
# ##   315572941     ###
# ######################
#
# ################################

import sys
import Project

class Error(Exception):  # Errors
    pass

class Start(Error):  # Use to print the main
    pass

class NotAnInput(Error):
    pass

class NoneFound(Error):
    pass

def print_menu():  # Print the menu
    print("menu")
    print("Please choose a question:")
    print("1.) Question 1")
    print("2.) Question 2")
    print("3.) Question 3")
    print("4.) Exit")


if __name__ == "__main__":  # Main of program
    loop = True
    while loop:
        try:
            print_menu()  # Menu
            question = int(input())  # Options - main
            if question == 1:
                loop = False  # Inner options
                ans = Nohar_Batit3.menu1()
                if ans == 1:
                    raise Start
                elif ans == 0:
                    sys.exit()
            elif question == 2:
                loop = False
                ans = Nohar_batit2.menu2()
                if ans == 1:
                    raise Start
                elif ans == 0:
                    sys.exit()
            elif question == 3:
                loop = False
                ans = Nohar_Batit4.menu3()  # Return to menu
                if ans == 1:
                    raise Start
                elif ans == 0:  # Exit the program
                    sys.exit()
            elif question == 4:
                print("Thank you!")
                sys.exit()
        except ValueError:
            print("Wrong choice. Try again")
        except Start:
            loop = True
