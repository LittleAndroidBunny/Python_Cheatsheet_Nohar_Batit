class Error(Exception):  # Errors
    pass

class NotAnInput(Error):
    pass

class NoneFound(Error):
    pass

class NoneList(Error):
    pass

def print_1():
    print("1.Add a list")
    print("2.Print the list")
    print("3.Print answer")
    print("4.Print menu")
    print("5.Exit")

num = []
list1 = []
def div_get_list():  # Print the request and save the values using append to a variable list1
    try:
        global list1, num
        number = int(input("Please enter the number of elements you want to insert:\n"))
        print("Enter the elements of your list, separated by enter:")
        list1 = [int(input()) for i in range(number)]
        num = [i for i in list1 if i % 3 == 0]
        return
    except:
        print("Only specified type allowed, try again:")
        list1.clear()
        div_get_list()

def check_num():  # Print the answer whether there is a number
    if not num:
        raise NoneFound("There is no number that divides by 3", NoneFound)  # If i need to print the error
    else:
        print(f"The first number in the list that divides by 3 is: {num[0]}")
    return


def menu1():  # This function acs as main program of question 1
    go = True
    while go:
        try:
            print_1()
            ans = int(input("What would you like to do?\n"))  # Options
            if ans == 1:
                div_get_list()  # Get
            elif ans == 2:  # Print the list
                if not list1:
                    raise NoneList
                else:
                    print(list1)
            elif ans == 3:
                check_num()
            elif ans == 4:
                return 1
            elif ans == 5:
                print("Thank you!")
                return 0
            else:
                raise NotAnInput
        except NoneFound:
            print("NoneFound:There is no number that divides by 3")
        except NotAnInput:
            print("Wrong choice. Try again")
        except ValueError:
            print("Wrong choice. Try again")
        except NoneList:
            print("NoneList: The list is empty.")
            go = True
        except:
            go = True
