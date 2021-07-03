import itertools

birthday_dict = {}
tr_sub = ['noy', 'shir', 'eli', 'tomer', 'jasper']  # use it when i need to print trainer for a subscriber
subs = ['dana', 'rona', 'lior', 'ofek', 'eyal']  # use it when i need to print subscriber for a trainer
classes = {}


class Gym:  # Parent class
    login_id = itertools.count()

    def __init__(self, name, gender, gym_name, birthday_val, permission):  # initializing
        self.name = name
        self.gender = gender
        self.gym_name = gym_name
        self.birthday_val = birthday_val
        self.permission = permission
        self.day, self.month, self.year = birthday_val.split('/')
        self.login_id = next(self.login_id)
        self.first, self.last = name.split(' ')

        if gender == "F":  # check what gender
            self.title = "Miss."
        elif gender == "M":
            self.title = "Mr."
        else:
            self.title = None
        if self.month in birthday_dict:  # add to print birthday of people from the same month
            birthday_dict[self.month].append(self.name)
        else:
            birthday_dict[self.month] = [self.name]
        if (permission == "S") or (permission == "s"):
            if self.name in subs:
                pass
            else:
                subs.append(self.name)
        elif (permission == "T") or (permission == "t"):
            if self.name in tr_sub:
                pass
            else:
                tr_sub.append(self.name)

    def __str__(self):
        pass

    def __add__(self, other):
        pass

    @property
    def full_name(self):
        return self.first, self.last

    @full_name.setter  # set name
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def email(self):
        return f"{self.first + self.last}@gmail.com"

    @property
    def birthday(self):
        return self.birthday_val

    @birthday.setter  # set birthday
    def birthday(self, birthday_val):
        pass

    def information(self):  # block of information
        return f"Full name: {self.title} {self.name}\n" \
               f"Login ID: {self.login_id}\n" \
               f"Permissions: {self.permission}\n" \
               f"Email: {self.email()}"
