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
    employee_counter = 1

    def __init__(self, role='', salary=0, **kwargs):
        super().__init__(**kwargs)
        self.role = role
        self.salary = salary
        self.employee_id = self.__class__.employee_counter
        self.__class__.employee_counter += 1

    def __str__(self):
        return f"--Employee file--\nEmployee_ID: {self.employee_id}\nName: {self.last_name}, {self.first_name}\nDOB:" \
               f" {self.dob}\nFunction: {self.role}"

    def change_role(self, new_role):
        self.role = new_role

    def change_salary(self, new_salary):
        self.salary = new_salary


class Teacher(Employee):

    def __init__(self, courses=None, **kwargs):
        super().__init__(**kwargs)
        self.courses = courses
        Headmaster.subordinates[self.__class__.__name__].append(self.last_name + ', ' + self.first_name)

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
        else:
            print(f"Sorry {course_name} is already on the list!")

    def remove_course(self, course_name):
        if len(self.courses) > 1:
            self.courses.remove(course_name)
        else:
            print("Error! At lease one course must be assigned to each teacher!")


class SupportStaff(Employee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Headmaster.subordinates[self.__class__.__name__].append(self.last_name + ', ' + self.first_name)


class Headmaster(Employee):
    subordinates = {item.__name__: [] for item in Employee.__subclasses__() if item.__name__ != 'Headmaster'}

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
        return f"--Student File--\nName:{self.last_name}, {self.first_name}\nDOB:{self.dob}\nYear: {self.year}\n" \
               f"Courses: {','.join(list(self.grade_book.keys()))}\nGrades: {self.grade_book}\nGPA: {self.get_gpa()}"

    def add_grade(self, course, grade):
        if 0 <= grade <= 100:
            self.grade_book[course].append(grade)
        else:
            print("Error! Please specify a value in range 0-100")

    def get_gpa(self):
        total = 0
        count = 0
        for item in list(self.grade_book.values()):
            for i in range(len(item)):
                total += item[i]
                count += len(item)
        gpa = round(total / count, 0)
        return gpa

    def add_course(self, new_course, course):
        if new_course not in self.courses:
            self.courses.append(new_course)
            self.grade_book[new_course]=[]
            course.students.append(self.last_name + ', ' + self.first_name)
        else:
            print("Error!Course already added!")

    def remove_course(self, course):
        if course.name in self.courses:
            self.courses.remove(course.name)
            self.grade_book.pop(course.name)
            course.students.remove(self.last_name + ', ' + self.first_name)
        else:
            print(f"Error! {course.name} is not on the list!")

    def list_courses(self):
        return '\n'.join(self.courses)


class Course:
    def __init__(self, name, max_students, time):
        self.name = name
        self.max_student = max_students
        self.students = []
        self.time = time

    def add_to_schedule(self, classroom):
        if not classroom.schedule[self.time]:
            classroom.schedule[self.time] = self.name
        else:
            print("Error! Time slot occupied. Choose another slot or room!")

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student.last_name+', '+student.first_name)
        else:
            print("Error! Maximum course capacity exceeded")

    def get_student_list(self):
        return '\n'.join(self.students)


class Room:
    def __init__(self, floor=None, number=None, room_type=None, **kwargs):
        self.floor = floor
        self.number = number
        self.room_type = room_type
        super().__init__(**kwargs)


class Classroom(Room):
    def __init__(self, capacity=None, **kwargs):
        super().__init__(**kwargs)
        self.schedule = {item: '' for item in range(8, 18)}
        self.capacity = capacity

    def check_schedule(self):
        return self.schedule

    # add class to schedule when class instantiated


class HeadmasterOffice(Room):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class UtilityRoom(Room):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Toilet(Room):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# headmaster instance:
# BreezeA = Headmaster(last_name='Breeze', first_name='Amanda', dob='1990-06-07', role='headmaster', salary=200000)

# teacher instances:
# RobinsonA = Teacher(last_name='Robinson', first_name='Ann', dob='1990-10-01', role='senior teacher', salary=150000,
#                     courses=['Mathematics'])
# SmithB = Teacher(last_name='Smith', first_name='Bill', dob='1991-12-12', role='teacher', salary=170000,
#                  courses=['Latin'])
# DionC = Teacher(last_name='Dion', first_name='Celine', dob='1995-04-14', role='junior teacher', salary=100000,
#                 courses=['English'])

# support staff instances:
# Jenkins = SupportStaff(last_name='Jenkins', first_name='Michael', dob='1980-05-01', role='janitor', salary=90000)
# Mendez = SupportStaff(last_name='Mendez', first_name='Jenna', dob='1999-10-10', role='nurse', salary=100000)

# print(Headmaster.subordinates)
# print(BreezeA.get_age())
# BreezeA.adjust_surname('Bree')
# print(BreezeA.get_surname())
# print(BreezeA.employee_id)
#
# print(RobinsonA.employee_id)
# print(RobinsonA.courses)
# RobinsonA.add_course('Mathematics')
# RobinsonA.add_course('Social sciences')
# print(RobinsonA.courses)
# RobinsonA.remove_course('Social sciences')
# print(RobinsonA.courses)

# student instances
# AfleckM = Student(last_name='Afleck', first_name='Mandy', dob='2008-07-15', year='7',
#                   courses=['English', 'Mathematics', 'History', 'Social Science'])
# BradfordL = Student(last_name='Bradford', first_name='Linda', dob='2008-12-15', year='7',
#                     courses=['English', 'Mathematics', 'Science', 'Pottery'])
# WachowskiB = Student(last_name='Wachowski', first_name='Brad', dob='2008-05-05', year='7',
#                      courses=['English', 'Mathematics', 'History', 'Art'])
# GonzalezA = Student(last_name='Gonzalez', first_name='Adam', dob='2008-01-01', year='7',
#                     courses=['English', 'Mathematics', 'History', 'Computer Science'])

# GonzalezA.add_grade('History', 90)
# GonzalezA.add_grade('History', 120)
# GonzalezA.add_grade('Mathematics', 95)
# GonzalezA.add_grade('English', 75)
# GonzalezA.add_grade('Computer Science', 100)
# print(GonzalezA.grade_book)
# print(GonzalezA.get_gpa())
# print(GonzalezA.list_courses())
# print(GonzalezA)
# print(GonzalezA.student_id)

# maths_lab = Classroom(floor=1, number=6, room_type='lab', capacity=25)
# print(maths_lab.schedule)
# maths = Course(name='Mathematics', max_students=3, time=10)
# art = Course(name='Art', max_students=10, time=15)
# pottery = Course(name='Pottery', max_students=5, time=16)
# maths.add_to_schedule(maths_lab)
# print(maths_lab.schedule)

# maths.add_student(GonzalezA)
# maths.add_student(AfleckM)
# maths.add_student(WachowskiB)
# print(maths.get_student_list())
# maths.add_student(BradfordL)

# GonzalezA.add_course('Art', art)
# GonzalezA.add_course('Pottery', pottery)
# print(GonzalezA.grade_book)
# print(GonzalezA.list_courses())
# print(art.students)
# print(pottery.students)
# GonzalezA.remove_course(art)
# print(GonzalezA.grade_book)
# print(GonzalezA.list_courses())
# print(art.students)
# # AfleckM.add_course('Art', art)
# print(AfleckM.grade_book)
# print(AfleckM.list_courses())
# print(art.students)


