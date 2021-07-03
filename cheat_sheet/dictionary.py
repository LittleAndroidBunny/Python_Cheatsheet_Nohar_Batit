# A dictionary is comprised of keys and values,
# the keys can be any immutable variable
d1 = {1: 'Apple', '2': 'Banana', 'C': 'Orange'}

print(d1)
# {1: 'Apple', '2': 'Banana', 'round': 'Orange'}

print(d1[1])
# Apple

print(d1['C'])
# Orange


d2 = {1: '1', 2: '2', 3: 3}     # keys can be any immutable object
d3 = {'office': 97286421234, 'fax': 97286421234, 'mobile': 972526421234}


# methods
d1 = dict()     # initialize an empty dictionary

for i in range(10):
    d1[i] = i

print(d1.get(10, 0))

for k, v in d3.items():
    print('The phone number at the ' + k + ' is ' + str(v) )

# example 1

students_lst = [['Assaf', 90], ['Yair', 80], ['Alon', 70]]


def get_student_grade1(students_lst, name):
    """find a student name in the list and return his grade

    :param students_lst: a list of lists of students names and grades
    :param name: the desired student name as string
    :return: the desired student grade if found ( default = None )
    """
    for student in students_lst:
        if student[0] == name:
            return student[1]
    return None


print(get_student_grade1(students_lst, 'Alon'))


student_dir = {'Assaf': 90, 'Yair': 80, 'Alon': 70}

print(student_dir.get('Alon'))
print(student_dir['Alon'])
print(student_dir.get('Moti'))
print(student_dir['Moti'])

students_dict = dict(students_lst)


# example 2

sqr = {x: x**2 for x in range(3, 11, 2)}


# example 3


phonebook_dict = {'meni': {'office': 97286421234, 'fax': 97286421234, 'mobile': 972526421234},
                  'jinji': {'office': 97286421234, 'mobile': 972526421234, 'email': "mail_address@gmail.com"}

                  }
print(phonebook_dict['meni']['office'])
print(phonebook_dict['jinji']['email'])

