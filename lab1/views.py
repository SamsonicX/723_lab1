# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        subjects = [
            Subject("timp"),
            Subject("eis"),
            Subject("philosophy"),
            Subject("english"),
            Subject("sport")
        ]

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

        list_score = Score()
        list_score.add_fixed(0, 4, 5, 3, 4, 2)
        list_score.add_fixed(1, 4, 5, 5, 5, 4)
        list_score.add_fixed(2, 4, 5, 5, 5, 4)
        list_score.add_fixed(3, 2, 3, 5, 5, 4)
        list_score.add_fixed(4, 2, 2, 3, 3, 2)
        list_score.add_fixed(5, 4, 5, 2, 5, 4)
        list_score.add_fixed(6, 4, 5, 5, 5, 4)
        list_score.add_fixed(7, 4, 5, 5, 3, 4)
        list_score.add_fixed(8, 2, 5, 5, 5, 4)
        list_score.add_fixed(9, 2, 1, 1, 1, 4)

        list_average = []
        for student_id in range(len(list_students)):
            counter = 0
            for subject_id in range(len(subjects)):
                counter += list_score(student_id * len(subjects) + subject_id).value
            list_average.append(counter / len(subjects))

        students_statistics = []
        for student in len(list_students):
            student_info = {
                'id': student_id + 1,
                'fio': student.familia + " " + student.imya + " " + student.otchestvo,
                'timp': list_score(student_id * len(subjects)).value,
                'eis': list_score(student_id * len(subjects) + 1).value,
                'philosophy': list_score(student_id * len(subjects) + 2).value,
                'sport': list_score(student_id * len(subjects) + 3).value,
                'average': list_average(student_id)
            }
            students_statistics.append(student_info)

        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': 1,
                        'fio': 'Someone',
                        'timp': 2,
                        'eis': 3,
                        'philosophy': 4,
                        'english': 5,
                        'sport': 2.3,
                        'average': 2.3,
                    }
                ],
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
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
    def __init__(self, name):
        self.list.append(name)


class Score:
    table = []

    def __init__ (self, st_id, sb_id, value):
        self.table.append((st_id, sb_id, value))

    def add_fixed(self, st_id, value1, value2, value3, value4, value5):
        self.table.append((st_id, 1, value1))
        self.table.append((st_id, 2, value2))
        self.table.append((st_id, 3, value3))
        self.table.append((st_id, 4, value4))
        self.table.append((st_id, 5, value5))