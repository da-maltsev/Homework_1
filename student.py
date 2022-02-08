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

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_course += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Peeta', 'Paka')
cool_lecturer.courses_attached += ['Python']
best_student.rate_lecture(cool_lecturer, 'Python', 7)
best_student.rate_lecture(cool_lecturer, 'Python', 3)
best_student.rate_lecture(cool_lecturer, 'Java', 5)

# # print(best_student.grades)
# print(cool_lecturer.grades)
# cool_lecturer.rate_hw()

print(cool_reviewer)
print(cool_lecturer)
print(best_student)