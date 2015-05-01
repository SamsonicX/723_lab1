# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Заполнение списка предметов
        subjects = [
            Subject(0, "timp"),
            Subject(1, "eis"),
            Subject(2, "philosophy"),
            Subject(3, "english"),
            Subject(4, "sport")
        ]

        # Заполнение списка студентов
        list_students = [
            Student(0, "surname1", "name1", "patronymic1", "group1", 20),
            Student(1, "surname2", "name2", "patronymic2", "group2", 20),
            Student(2, "surname3", "name3", "patronymic3", "group2", 20),
            Student(3, "surname4", "name4", "patronymic4", "group1", 20),
            Student(4, "surname5", "name5", "patronymic5", "group1", 20),
            Student(5, "surname6", "name6", "patronymic6", "group3", 20),
            Student(6, "surname7", "name7", "patronymic7", "group3", 20),
            Student(7, "surname8", "name8", "patronymic8", "group2", 20),
            Student(8, "surname9", "name9", "patronymic9", "group1", 20),
            Student(9, "surname10", "name10", "patronymic10", "group1", 20),
        ]

        # Заполнение массива оценок случайными значениями от 2 до 5
        from random import randint
        list_score = []
        for student_id in range(len(list_students)):
            for subject_id in range(len(subjects)):
                list_score.append(Score(student_id, subject_id, randint(2, 5)))

        list_student_average = []  # Лист средних оценок на студента
        excellent_students = ' '  # Строка со студентами, которых надо будет похвалить (в ней будет ТОЛЬКО фамилия)
        bad_students = ' '  # Строка со студентами, которых надо будет отчислить (в ней будет ТОЛЬКО фамилия)
        counter_subjects = [0.] * len(subjects)  # Лист средних оценок на предметы

        # Цикл, расчитывающий среднее значение оценки у студента. Так же идёт суммирование всех оценок по предметам
        for student_id in range(len(list_students)):
            counter_st = 0.
            for subject_id in range(len(subjects)):
                counter_st += list_score[student_id * len(subjects) + subject_id].value
                counter_subjects[subject_id] += list_score[student_id * len(subjects) + subject_id].value
            list_student_average.append(counter_st / len(subjects))
            if list_student_average[student_id] > 4.5:
                excellent_students += (list_students[student_id].person.familia) + ' '
            if list_student_average[student_id] < 3:
                bad_students += (list_students[student_id].person.familia) + ' '

        # Нахождение среднего значения по предмету (в counter_subjects до этого были только сумма оценок по предмету)
        for subject_id in range(len(subjects)):
            counter_subjects[subject_id] /= len(list_students)

        # Сопоставление статистики
        students_statistics = []
        for student_id in range(len(list_students)):
            student_info = {
                'id': student_id + 1,
                'fio': list_students[student_id].person.familia + ' ' + list_students[student_id].person.imya + ' ' + list_students[student_id].person.otchestvo,
                'timp': list_score[student_id * len(subjects)].value,
                'eis': list_score[student_id * len(subjects) + 1].value,
                'philosophy': list_score[student_id * len(subjects) + 2].value,
                'english': list_score[student_id * len(subjects) + 3].value,
                'sport': list_score[student_id * len(subjects) + 4].value,
                'average': list_student_average[student_id]
            }
            students_statistics.append(student_info)

        subjects_info = {
            'id': '',
            'fio': 'Итого',
            'timp': counter_subjects[0],
            'eis': counter_subjects[1],
            'philosophy': counter_subjects[2],
            'english': counter_subjects[3],
            'sport': counter_subjects[4]
        }
        students_statistics.append(subjects_info)

        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': students_statistics,
                'excellent_students': excellent_students,
                'bad_students': bad_students
            }
        )
        return context


class Person:
    def __init__(self, familia, imya, otchestvo):
        self.familia = familia
        self.imya = imya
        self.otchestvo = otchestvo

class Student(Person):
    def __init__(self, student_id, familia, imya, otchestvo, group, age):
        self.student_id = student_id
        self.person = Person(familia, imya, otchestvo)
        self.group = group
        self.age = age


class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Score:
    def __init__(self, student_id, subject_id, value):
        self.student_id = student_id
        self.subject_id = subject_id
        self.value = value