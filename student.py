from statistics import mean
def avg(dictionary):
    lst = dict.values(dictionary)
    lst_unpacked = [x for l in lst for x in l]
    value = sum(lst_unpacked)
    numbers = len(lst_unpacked)
    average = value/numbers
    return average

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_course = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and\
        course in lecturer.courses_attached :
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg(self.grades)}')
        print('Курсы в процессе изучения: ', end='')
        print(', '.join(self.courses_in_progress))
        print('Завершенные курсы: ', end='')
        print(', '.join(self.finished_course))

    def __lt__(self, other):
        return avg(self.grades)<avg(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self):
        print('У лектора нет прав для выставления оценки')

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg(self.grades)}')

    def __lt__(self, other):
        return avg(self.grades)<avg(other.grades)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')

def avg_grade_student(student_list, course):
    grade = []
    for student in student_list:
        for key_, value_ in student.grades.items():
            if key_ == course:
                for grades in value_:
                    grade.append(grades)
    avg_grade = mean(grade)
    return avg_grade

def avg_grade_lecturer(lecturer_list, course):
    grade = []
    for lecturer in lecturer_list:
        for key_, value_ in lecturer.grades.items():
            if key_ == course:
                for grades in value_:
                    grade.append(grades)
    avg_grade = mean(grade)
    return avg_grade

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_course += ['Введение в программирование']

worst_student = Student('Ruoy', 'Eman', 'your_gender')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Java']
worst_student.finished_course += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
fool_reviewer = Reviewer('Big', 'Smoke')
fool_reviewer.courses_attached += ['Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
fool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(worst_student, 'Python', 1)
cool_reviewer.rate_hw(worst_student, 'Python', 5)
fool_reviewer.rate_hw(worst_student, 'Java', 7)

cool_lecturer = Lecturer('Peeta', 'Paka')
cool_lecturer.courses_attached += ['Python']
best_student.rate_lecture(cool_lecturer, 'Python', 7)
best_student.rate_lecture(cool_lecturer, 'Python', 3)
best_student.rate_lecture(cool_lecturer, 'Java', 5)

fool_lecturer = Lecturer('Peeta', 'Paka')
fool_lecturer.courses_attached += ['Python']
best_student.rate_lecture(fool_lecturer, 'Python', 4)
best_student.rate_lecture(fool_lecturer, 'Python', 3)
best_student.rate_lecture(fool_lecturer, 'Java', 5)

print(best_student.grades)
print(cool_lecturer.grades)
cool_lecturer.rate_hw()

# print(cool_reviewer)
# print(cool_lecturer)
# print(best_student)
print(cool_lecturer>fool_lecturer)
print(best_student>worst_student)
print(avg_grade_student([best_student, worst_student], 'Java'))
print(avg_grade_lecturer([cool_lecturer, fool_lecturer], 'Python'))