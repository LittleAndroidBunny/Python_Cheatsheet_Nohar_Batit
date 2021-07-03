import random
from Nohar_Batit3 import Gym
from Nohar_Batit3 import subs
from Nohar_Batit3 import tr_sub
from Nohar_Batit3 import classes

class Error(Exception):  # Errors
    pass


class Start(Error):  # Use to print the main
    pass


class NotAnInput(Error):
    pass


class NoneFound(Error):
    pass


def print_2():  # menu of class
    print("Hello trainer, what would you like to do?")
    print("1. add your details")
    print("2. print your details")
    print("3. get your shifts")
    print("4. get trainees list")
    print("5. print main menu")
    print("6. Exit")


weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")  # when needed to get schedule


class Trainers(Gym):
    def __init__(self, name, gender, gym_name, birthday_val, permission, salary):
        super().__init__(name, gender, gym_name, birthday_val, permission)
        self.salary = int(salary)
        self.trainee_1 = []

    def shifts(self):  # get wanted salary and compute weekdays methode
        if 1000 > self.salary:
            return random.choices(weekDays, k=1)
        elif 1000 <= self.salary <= 2500:
            return random.choices(weekDays, k=3)
        elif self.salary > 2500:
            return random.choices(weekDays, k=5)
        else:
            raise AssertionError


    def trainee(self):  # ask for salary to determine responsibility
        if len(subs) < 5:
            return "Not enough sub. i create for you: dana, loren, mila"
        else:
            if 1000 > self.salary:
                if self.name in tr_sub:
                    return tr_sub[self.name]
                elif self.name not in tr_sub:
                    tr_sub[self.name] = [random.choices(subs, k=3)]
                    return tr_sub[self.name]
            elif 1000 <= self.salary <= 2500:
                if self.name in tr_sub:
                    return tr_sub[self.name]
                elif self.name not in tr_sub:
                    tr_sub[self.name] = [random.choices(subs, k=5)]
                    return tr_sub[self.name]
            else:
                raise AssertionError


def run2():  # running as bot
    test2 = Trainers('alon rocheeld', 'M', 'Fitness club', "7/5/1991", 'T', 3500)
    print(f'Example object:\n{test2.information()}')
    go = True
    while go:
        try:
            print_2()
            ans = int(input())  # options
            if ans == 1:
                name = input("Enter your first name\n")  # set a new object
                classes[name] = Trainers(input("Enter your full name using space:\n"),
                                         input("Enter your gender: F or M \n"), "Fitness club",
                                         input("Enter your birthday, for example: 1/1/2021"), "T",
                                         input("Enter desired salary:"))
            elif ans == 2:
                name_choose = input("Enter your first name as inserted:")
                if isinstance(classes[name_choose], Trainers):
                    print(classes[name_choose].information())
                else:
                    raise NoneFound
            elif ans == 3:
                name_choose = input("Enter your first name as inserted:")
                if isinstance(classes[name_choose], Trainers):
                    print(classes[name_choose].shifts())
                else:
                    raise NoneFound
            elif ans == 4:
                name_choose = input("Enter your first name as inserted:")
                if isinstance(classes[name_choose], Trainers):
                    print(classes[name_choose].trainee())
                else:
                    raise NoneFound
            elif ans == 5:
                return 1
            elif ans == 6:
                print("Thank you!")
                return 0
            else:
                raise NotAnInput
        except NoneFound:
            print("No details found.")
        except ValueError:
            print("Wrong choice. Try again")
        except AssertionError:
            print("AssertionError: This is not an Subscribers data")
        except:
            go = True
