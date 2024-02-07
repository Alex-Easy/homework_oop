# -*- coding: utf-8 -*-

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        finished_courses = ', '.join(self.finished_courses)
        courses_in_progress = ', '.join(self.courses_in_progress)
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grade_hw()} \nКурсы в процессе изучения: {courses_in_progress} \nЗавершенные курсы: {finished_courses}'

    def avg_grade_hw(self):
        for course, grades in self.grades.items():
            return f'{round(sum(grades) / len(grades), 1)}'

    def __lt__(self, other):
        return self.avg_grade_hw() < other.avg_grade_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()}'

    def avg_grade(self):
        for course, grades in self.grades.items():
            return f'{round(sum(grades) / len(grades), 1)}'

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()


best_student = Student('Roy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Основы языка Python']

student_1 = Student('Bill', 'Gates', 'male')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Основы GIT']

student_2 = Student('Elon', 'Musk', 'male')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['OOП в языке Python']

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Python', 'Git']

lecturer_1 = Lecturer('Guido', 'Rossum')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Steve', 'Jobs')
lecturer_2.courses_attached += ['Python', 'Git']

reviewer_1 = Reviewer('Tom', 'Hanks')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Tim', 'Burton')
reviewer_2.courses_attached += ['Python', 'Git']

best_mentor = Reviewer('Jane', 'Air')
best_mentor.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)

best_student.rate_lecturer(best_lecturer, 'Python', 9)
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 7)

best_mentor.rate_hw(best_student, 'Python', 10)
best_mentor.rate_hw(best_student, 'Python', 10)
best_mentor.rate_hw(best_student, 'Python', 10)

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 6)
student_1.rate_lecturer(lecturer_1, 'Python', 8)

student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 8)

print(best_mentor)
print(best_lecturer)
print(best_student)

print(student_2 > student_1)
print(lecturer_1 < lecturer_2)

print(student_1)
print(student_2)

print(lecturer_1)
print(lecturer_2)

print(reviewer_1)
print(reviewer_2)

students_list = [student_1, student_2, best_student]

def avg_grade_all_students(student_list, course):
    for student in students_list:
        if course in student.grades:
            return f'{round(sum(student.grades[course]) / len(student.grades[course]), 1)}'
        else:
            return 'Ошибка'


lecturers_list = [best_lecturer, lecturer_1, lecturer_2]

def avg_grade_all_lectors(lecturers_list, course):
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            return f'{round(sum(lecturer.grades[course]) / len(lecturer.grades[course]), 1)}'
        else:
            return 'Ошибка'


print(avg_grade_all_students(students_list, 'Python'))
print(avg_grade_all_lectors(lecturers_list, 'Python'))
