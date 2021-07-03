
class Student:
    """
    This class holds a student in the BGU systems.
    """
    affiliations = ["BGU"]

    def __init__(self, name, phone_number, id_number):
        self.name = name
        self.phone_number = phone_number
        self.id_number = id_number
        self.average_grade = -1
        self.current_courses = []
        self.grade_sheet = dict()
        self.phone_number = ''

    def enroll_course(self, course_name):
        self.current_courses.append(course_name)

    def drop_course(self, course_name, grade=None):
        self.current_courses.pop(self.current_courses.index(course_name))
        if grade:
            self.grade_sheet[course_name] = grade
        else:
            self.grade_sheet[course_name] = 700  # not complete

    def add_grade_to_course(self, course_name, grade):
        self.drop_course(course_name, grade)
        self.calculate_average_grade()

    def get_student_name(self):
        return self.name

    def send_email_to_student(self, string):
        # Todo
        pass

    def calculate_average_grade(self):
        self.average_grade = self._calculate_average_()

    def _calculate_average_(self):
        sum = 0
        for grade in self.grade_sheet.values():
            sum = sum + grade
        return sum/len(self.grade_sheet.values())

if __name__ == '__main__':
    student = Student('Yossi', '0501234567', '200456789')
    print(student.name)
    print(student.get_student_name())
    student.enroll_course('Python')
    student.enroll_course('ICS')
    student.enroll_course('Calculus 1')
    student.enroll_course('English level two')
    print(student.current_courses)
    student.add_grade_to_course('Python', 100)
    student.drop_course('Calculus 1')
    student.add_grade_to_course('English level two', 62)
    print(student.current_courses)
    print(student.grade_sheet)
    student.affiliations.append("HUJI")
    print(student.affiliations)
    s1 = Student('Beni', '1234', '987')
    print(s1.affiliations)
