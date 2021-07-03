import random
from Nohar_Batit3 import Gym
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


def print_3():  # menu of class
    print("Hello subscriber, what would you like to do?")
    print("1. add my detailes")
    print("2. print your details")
    print("3. get a trainer")
    print("4. get a program")
    print("5. return main menu")
    print("6. exit")


class Subscribers(Gym):  # subclass of Gym
    def __init__(self, name, gender, gym_name, birthday_val, permission, goal):
        super().__init__(name, gender, gym_name, birthday_val, permission)
        self.goal = goal

    def get_trainer_details(self):  # random value methode
        return f"Your trainer is: {random.choice(tr_sub)}"

    def get_program(self):  # can compute program to achieve goal
        if self.goal == "weight loss":
            print("Breakfast: scrambled eggs, stir-fried veggies, and oatmeal\n"
                  "Snack: whey protein shake\n"
                  "Lunch: grilled chicken breast, mixed greens, and baked sweet potato\n"
                  "Snack: hard-boiled egg(s) and carrot sticks\n"
                  "Dinner: broiled fish, green beans with brown rice\n"
                  "Exercises:3X Assisted lunges\n"
                  "3X Modified pushups\n"
                  "3X Ball squats\n"
                  "3X Overhead presses\n"
                  "3X Dumbbell rows\n"
                  "3X Bicep curls\n"
                  "3X Tricep extensions\n"
                  "3X Crunches on the ball\n"
                  "3X Back extensions")
        elif self.goal == "maintain":
            print("Breakfast: Scrambled Egg\n"
                  "           Whole Grain Toast\n"
                  "           Smoothie\n"
                              "Lunch: Grilled chicken vegetable roti rolls\n"
                              "Dinner: Chicken Stir Fry\n"
                              "Exercises:30-minute cardio\n"
                              "total-body strength level 2;\n"
                              "perform each exercise for 2 sets of 15 reps, resting 20 to 30 seconds between sets.\n"
                              "Interval workout level 3\n"
                              "Yoga on the ball\n"
                              "total-body strength level 2; perform each exercise for 2 sets of 15 reps, "
                              "resting 20 to 30 seconds between sets.\n"
                              "30-minute cardio")
        elif self.goal == "muscle gain":
            print("Meal 1: Contains starchy carbs\n"
                  'Meal 2: Few carbs, if any\n'
                  'Meal 3: Few carbs, if any\n'
                  'Meal 4: (Post-Workout Nutrition) Contains starchy carbs\n'
                  'Meal 5: Contains starchy carbs\n'
                  "Exercises:Squats\n"
                  '3 sets of 6-8 reps.\n'
                  '2-3 minutes rest between sets.\n'
                  'Split Squats\n'
                  '3 sets of 8-10 reps.\n'
                  '1-2 minutes rest between sets.\n'
                  'Lying Leg Curls\n'
                  '3 sets of 10-12 reps.\n'
                  '1-2 minutes rest between sets.\n'
                  'Seated Calf Raises\n'
                  '4 sets of 10-15 reps.\n'
                  '1-2 minutes rest between sets.\n'
                  'Abs\n'
                  'x sets of 8-15 reps.\n'
                  '1 minute rest between sets.')


def run3():  # running as bot
    test3 = Subscribers('adam hava', 'M', 'Fitness club', "1/8/1991", 'S', 'weight loss')
    print(f'Example object:\n{test3.information()}')
    go = True
    while go:
        try:
            print_3()
            ans = int(input())  # options
            if ans == 1:
                name = input("Enter your first name\n")
                classes[name] = Subscribers(input("Enter your full name using space:\n"), input("Enter your gender: F "
                                                                                                "or M \n"),
                                            "Fitness club", input("Enter your birthday, for example: 1/1/2021\n"),
                                            "S", input("Enter your goal: maintain, weight loss or muscle gain:\n"))
            elif ans == 2:
                name_choose = input("Enter your first name as inserted:")
                if isinstance(classes[name_choose], Subscribers):
                    print(classes[name_choose].information())
                else:
                    raise NoneFound
            elif ans == 3:
                name_choose = input("Enter your first name as inserted:")
                if isinstance(classes[name_choose], Subscribers):
                    print(classes[name_choose].get_trainer_details())
                else:
                    raise NoneFound
            elif ans == 4:
                name_choose = input("Enter your first name as inserted:")
                if isinstance(classes[name_choose], Subscribers):
                    classes[name_choose].get_program()
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
