# This script is part of tutorial number 4 of introduction of computer science for EE students at BGU.
# Topics:
#   - nested lists
#   - functions with list arguments

from typing import List, Union


def add_person(book: list, person: List[Union[str, list]]):
    """
    add a person to the phone book
    :param List book: phone book
    :param List[str, list] person: list containing person to add
    """
    if len(person) < 2 or type(person[0]) != str or type(person[1]) != list:
        raise TypeError("unexpected type for person")
    if type(book) != list:
        raise TypeError("book is expected to be a list")
    book.append(person)


def find_person_by_name(book: list, person_name: str) -> list:
    """
    return a list of phone numbers for a person, return empty list if not found

    :param List book: phone book
    :param str person_name: person name to look up
    :return: list of phone numbers for a person, return empty list if not found
    :rtype: list
    """
    # first obtain a list of names by "List comprehension"
    return [x[1] for x in book if x[0] == person_name]


def remove_person_by_name(book: list, person_name: str):
    """
       removes a person from phone book if found

       :param List book: phone book
       :param str person_name:
       """
    # bad code! - what happens if we look to for a missing number? error!
    # book.remove([x for x in book if x[0] == person_name][0])

    # Good code! - check existence first
    if person_name in [x[0] for x in book if x[0] == person_name]:
        book.remove([x for x in book if x[0] == person_name][0])


# declare the phone book
phone_book = list()

# add a person with one number
add_person(phone_book, ['Tom', ['026727448']])

# add a person with two numbers
add_person(phone_book, ['Jerry', ['026719715', '0546374756']])

# add two more
add_person(phone_book, ['Donald', ['036766809']])
add_person(phone_book, ['Duck', ['096446127']])

# find number by person name
jerry_number = find_person_by_name(phone_book, 'Jerry')
# what happens if we look to for a missing number?
peter_number = find_person_by_name(phone_book, 'Peter Pan')

# Remove a person by name
remove_person_by_name(phone_book, 'Donald')
remove_person_by_name(phone_book, 'Peter Pan')
pass
