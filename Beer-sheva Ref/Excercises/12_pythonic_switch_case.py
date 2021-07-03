def get_number_of_vowels(user_input: str):
    return user_input


def get_perfect_number(user_input: str):
    return 2*user_input


def get_lazy_caterer_number(user_input: str):
    return 3*user_input


if __name__ == '__main__':
    arg = 'dummy'
    task1 = 'vowels'
    task2 = 'typo'
    tasks_dict = {'vowels': lambda x: get_number_of_vowels(x), 'perfect': lambda x: get_perfect_number(x),
                  'lazy': lambda x: get_lazy_caterer_number(x)}
    print(tasks_dict.get(task1, lambda x: 'wrong input')(arg))
    print(tasks_dict.get(task2, lambda x: 'wrong input')(arg))
