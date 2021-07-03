class Student:
    """
    This class holds a student in the BGU systems.
    """
    current_courses = []

    def __init__(self, name, phone_number, id_number):
        self.name = name
        self.phone_number = phone_number
        self.id_number = id_number
        self.average_grade = -1


class StudentList:
    students = []

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self) -> Student:
        if self.current < len(self.students):
            res = self.students[self.current]
            self.current += 1
            return res
        else:
            raise StopIteration

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError('can only accept students')
        self.students.append(student)


if __name__ == '__main__':
    student_list = StudentList()
    student_list.add_student(Student('Yosi', '0501234567', '200456789'))
    student_list.add_student(Student('Moti', '0501765432', '2005685763'))
    for student in student_list:
        print(student.name)
