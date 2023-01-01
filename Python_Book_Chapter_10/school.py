"""
Design a class structure (incl. arguments and methods) for a primary school.
"""
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Person:
    def __init__(self, first_name='', last_name='', dob='', **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        super().__init__(**kwargs)

    def __str__(self):
        return f"Name: {self.last_name}, {self.first_name}\n DOB: {self.dob}"

    def get_name(self):
        return self.first_name

    def get_surname(self):
        return self.last_name

    def get_age(self):
        today = date.today()
        age = relativedelta(today, datetime.strptime(self.dob, '%Y-%m-%d')).years
        return age

    def adjust_name(self, correct_name):
        self.first_name = correct_name

    def adjust_surname(self, correct_last_name):
        self.last_name = correct_last_name

    def adjust_dob(self):
        while True:
            try:
                correct_dob = datetime.strptime(input("New dob: "), '%Y-%m-%d')
                self.dob = correct_dob
            except ValueError:
                print("Please provide dob in correct format yyyy-mm-dd")


class Employee(Person):
    empl_counter = 1

    def __init__(self, role='', salary=0, **kwargs):
        super().__init__(**kwargs)
        self.role = role
        self.salary = salary
        self.employee_id = self.__class__.empl_counter
        self.__class__.empl_counter += 1

    def __str__(self):
        return f"--Employee file--\nEmployee_ID: {self.employee_id}\nName: {self.last_name}, {self.first_name}\nDOB:" \
               f" {self.dob}\nFunction: {self.role}"

    def change_role(self, new_role):
        self.role = new_role

    def get_current_salary(self):
        return self.salary

    def change_salary(self, new_salary):
        self.salary = new_salary

class Teacher(Employee):

    def __init__(self, courses=None, **kwargs):
        super().__init__(**kwargs)
        self.courses = courses
        Headmaster.subordinates[self.__class__.__name__].append(self.last_name + ', ' + self.first_name)

    def add_course(self, course_name):
        try:
            if course_name not in self.courses:
                self.courses.append(course_name)
        except:
            raise Exception(f"Sorry {course_name} is already on the list")

    def remove_course(self, course_name):
        try:
            if len(self.courses) > 1:
                self.courses.remove(course_name)
        except:
            raise Exception("Error! At lease one course must be assigned to each teacher!")


class SupportStaff(Employee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Headmaster.subordinates[self.__class__.__name__].append(self.last_name+', '+self.first_name)


class Headmaster(Employee):
    subordinates = {item.__name__:[] for item in Employee.__subclasses__() if item.__name__ != 'Headmaster'}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Student(Person):
    student_counter = 1

    def __init__(self, year='', courses=None, **kwargs):
        super().__init__(**kwargs)
        self.student_id = self.__class__.student_counter
        self.__class__.student_counter += 1
        self.year = year
        self.courses = courses
        self.grade_book = {course: [] for course in self.courses}

    def __str__(self):
        return f"--Student File--\nName:{self.last_name}, {self.first_name}\nDOB:{self.dob}\n Year: {self.year}\n" \
               f"Courses: {list(self.grade_book.keys())}, Grades: {self.grade_book}, CPA: {self.get_gpa()}"

    def get_current_year(self):
        return self.year

    def add_grade(self, course, grade):
        try:
            if 0 < grade < 100:
                self.grade_book[course].append(grade)
        except:
            raise Exception("Error! Please specify a value in range 0-100")

    def get_gpa(self):
        return sum(list(self.grade_book.values())) / len(list(self.grade_book.values()))

    def add_course(self, course):
        try:
            if course not in self.courses:
                self.courses.append(course)
                self.grade_book.update((course, []))

        except:
            raise Exception("Error!Course already on the list")

    def get_courses(self):
        return ''.join(self.courses)


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_student = max_students
        self.students = []

    def add_student(self, student):
        try:
            if len(self.students) < self.max_student:
                self.students.append(student)
        except:
            raise Exception("Error! Maximum course capacity exceeded")

    def get_student_list(self):
        return '\n'.join(self.students)

    def get_avg_grade(self):
        total = 0
        for student in self.students:
            total += student.grade_book[self.name]
        return total / len(self.students)


RobinsonA = Teacher(last_name='Robinson', first_name='Ann', dob='1990-10-01', role='senior teacher', salary=150000,
                    courses=['Mathematics'])
SmithB = Teacher(last_name='Smith', first_name='Bill', dob='1991-12-12', role='teacher', salary=170000,
                 courses=['Latin'])
Jenkins = SupportStaff(last_name='Jenkins', first_name='Michael', dob='1980-05-01', role='janitor', salary=90000)
Menora = SupportStaff(last_name='Menora', first_name='Jenna', dob='1999-10-10', role='nurse', salary=100000)


print(Headmaster.subordinates)