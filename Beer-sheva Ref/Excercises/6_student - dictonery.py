
def enroll_course(student, course_name):
    student['current_courses'].append(course_name)


def drop_course(student, course_name, grade=None):
    student['current_courses'].pop(student['current_courses'].index(course_name))
    if grade:
        student['grade_sheet'][course_name] = grade
    else:
        student['grade_sheet'][course_name] = 700  # not complete


def add_grade_to_course(student, course_name, grade):
    drop_course(student, course_name, grade)
    calculate_average_grade(student)


def calculate_average_grade(student):
    sum = 0
    for grade in student['grade_sheet'].values():
        if grade == 700:
            continue
        sum = sum + grade
    student['average'] = sum / len(student['grade_sheet'].values())


def send_email_to_student(student, string):
    # Todo
    pass


if __name__ == '__main__':
    name = input('Please enter the student name: ')
    phone_number = input("Please enter the student's phone number: ")
    id_number = input("Please enter the student's id number: ")

    student = {'name': name, 'phone_number': phone_number, 'id': id_number, 'current_courses': [], 'grade_sheet': {},
               'average': -1}
    print(student['name'])
    enroll_course(student, 'Python')
    enroll_course(student, 'ICS')
    enroll_course(student, 'Calculus 1')
    enroll_course(student, 'English level two')

    print(student['current_courses'])
    add_grade_to_course(student, 'Python', 100)
    add_grade_to_course(student, 'English level two', 62)
    drop_course(student, 'Calculus 1')
    print(student['current_courses'])
    print(student['grade_sheet'])
    print(student['average'])
