class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.ag = None

    def rate_hw(self, lecturer, course, grade):

        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        eg = []
        for gr in self.grades.values():
            eg += gr
        self.ag = sum(eg) / len(eg)

    def __str__(self):
        return (
            f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{round(self.ag, 1)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.ag = None

    def average_grade(self):
        eg = []
        for gr in self.grades.values():
            eg += gr
        self.ag = sum(eg) / len(eg)

    def __gt__(self, lecturer):
        return (self.ag > lecturer.ag)

    def __str__(self):
        return (f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{round(self.ag, 1)}\n')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.ag = None

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]

            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'\nИмя: {self.name}\nФамилия: {self.surname}\n')


some_lecturer = Lecturer('Some', 'Buddy')  # лекторы
some_lecturer.courses_attached = ['Python', 'Git', 'Введение в программирование', 'SQL']

some_lecturer_2 = Lecturer('Edward', 'Cullen')
some_lecturer_2.courses_attached = ['Python', 'Git', 'Введение в программирование', 'SQL']

some_student = Student('Ruoy', 'Eman')  # студенты
some_student.courses_in_progress = ['Python', 'Git', 'SQL']
some_student.finished_courses = ['Введение в программирование']

some_student_2 = Student('Robert', 'Downey Jr.')
some_student_2.courses_in_progress = ['Python', 'Git']
some_student_2.finished_courses = ['Введение в программирование', 'SQL']

some_reviewer = Reviewer('Some', 'Buddy')  # ревьюверы
some_reviewer.courses_attached = ['Python', 'Git', 'Введение в программирование', 'SQL']

some_reviewer_2 = Reviewer('Lady', 'Gaga')
some_reviewer_2.courses_attached = ['Python', 'Git', 'Введение в программирование', 'SQL']

some_reviewer.rate_hw(some_student, 'Python', 10)  # оценки студента 1
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Введение в программирование', 9)
some_reviewer.rate_hw(some_student, 'SQL', 10)

some_reviewer_2.rate_hw(some_student, 'Python', 10)
some_reviewer_2.rate_hw(some_student, 'Git', 9)
some_reviewer_2.rate_hw(some_student, 'Введение в программирование', 10)
some_reviewer_2.rate_hw(some_student, 'SQL', 10)

some_reviewer.rate_hw(some_student_2, 'Python', 10)  # оценки студента 2
some_reviewer.rate_hw(some_student_2, 'Git', 10)
some_reviewer.rate_hw(some_student_2, 'Введение в программирование', 9)
some_reviewer.rate_hw(some_student_2, 'SQL', 10)

some_reviewer_2.rate_hw(some_student_2, 'Python', 10)
some_reviewer_2.rate_hw(some_student_2, 'Git', 10)
some_reviewer_2.rate_hw(some_student_2, 'Введение в программирование', 9)
some_reviewer_2.rate_hw(some_student_2, 'SQL', 10)

some_student.average_grade()  # средний балл студентов
some_student_2.average_grade()

some_student.rate_hw(some_lecturer, 'Python', 10)  # оценки лекторов
some_student.rate_hw(some_lecturer, 'Git', 10)
some_student.rate_hw(some_lecturer, 'Введение в программирование', 9)
some_student.rate_hw(some_lecturer, 'SQL', 9)

some_student.rate_hw(some_lecturer_2, 'Python', 10)
some_student.rate_hw(some_lecturer_2, 'Git', 10)
some_student.rate_hw(some_lecturer_2, 'Введение в программирование', 10)
some_student.rate_hw(some_lecturer_2, 'SQL', 9)

some_student_2.rate_hw(some_lecturer, 'Python', 10)
some_student_2.rate_hw(some_lecturer, 'Git', 10)
some_student_2.rate_hw(some_lecturer, 'Введение в программирование', 10)
some_student_2.rate_hw(some_lecturer, 'SQL', 10)
some_student_2.rate_hw(some_lecturer_2, 'Python', 10)
some_student_2.rate_hw(some_lecturer_2, 'Git', 10)
some_student_2.rate_hw(some_lecturer_2, 'Введение в программирование', 10)
some_student_2.rate_hw(some_lecturer_2, 'SQL', 10)

some_lecturer.average_grade()  # средний балл лекторов
some_lecturer_2.average_grade()

print('Ревьюверы:', some_reviewer, some_reviewer_2)  # принты

print('Лекторы:', some_lecturer, some_lecturer_2)

print('Студенты:', some_student, some_student_2)

if (some_lecturer > some_lecturer_2):
    print(some_lecturer.name + ' ' + some_lecturer.surname, "- самый крутой лектор!!!")
else:
    print(some_lecturer_2.name + ' ' + some_lecturer_2.surname, "- самый крутой лектор!!!")

print()


def lect_ag(lect_grades, lect_2_grades):  # функция для лекторов
    all_grades = {}
    for grade in lect_grades.items():
        all_grades[grade[0]] = grade[1]
    for grade in lect_2_grades.items():
        all_grades[grade[0]] += grade[1]
        all_grades[grade[0]] = sum(all_grades[grade[0]]) / len(all_grades[grade[0]])

    for k, v in all_grades.items():
        print('Средняя оценка лекторов по курсу', k, '-', v)


lect_ag(some_lecturer.grades, some_lecturer_2.grades)

print()


def stud_ag(stud_grades, stud_2_grades):  # функция для студентов
    all_grades = {}
    for grade in stud_grades.items():
        all_grades[grade[0]] = grade[1]
    for grade in stud_2_grades.items():
        all_grades[grade[0]] += grade[1]
        all_grades[grade[0]] = sum(all_grades[grade[0]]) / len(all_grades[grade[0]])

    for k, v in all_grades.items():
        print('Средняя оценка cтудентов по курсу', k, '-', v)


stud_ag(some_student.grades, some_student_2.grades)