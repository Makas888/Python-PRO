class Person:

    def __init__(self, name: str, surname: str, age: int, city: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city

    def output(self):
        return f'{self.name} {self.surname}, years: {self.age}, from {self.city}'

    def __str__(self):
        return f'{self.surname} {self.name[0]}: {self.age} years'


class Student(Person):

    def __init__(self, major: str, name: str, surname: str, age: int, city: str):
        super().__init__(name, surname, age, city)
        self.major = major

    def output(self):
        res = super().output()
        return f'{res} ==> student ({self.major})'

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Group:

    def __init__(self, course: str):
        self.course = course
        self.list_group = []
        self.status = 'Набор открыт'

    def add_student(self, student: Student):
        if isinstance(student, Student):
            if len(self.list_group) < 10 and self.list_group.count(student) <= 1:
                self.status = 'Набор открыт'
                self.list_group.append(student.__dict__)
            if len(self.list_group) >= 10:
                self.status = 'Набор группы закрыт'

    def delete_student(self, student: Student):
        if isinstance(student, Student):
            self.list_group.remove(student.__dict__)
            self.status = 'Набор открыт'

    def search_student(self, surname: str):
        if isinstance(surname, str):
            for student in self.list_group:
                if surname in student['surname']:
                    return f'{dict(student)["name"]} {dict(student)["surname"]},' \
                           f' {dict(student)["age"]} лет, {self.course}, из ' \
                           f'{dict(student)["city"]}, специальность - {dict(student)["major"]}'
            return '-1'

    def __str__(self):
        res = f'{self.status}! {self.course}:'
        for student in self.list_group:
            res += f'\n{student["surname"]} {student["name"][0]}.'

        return res


st_1 = Student('Developer', 'Андрей', 'Николаев', 24, 'Львов')
st_2 = Student('Developer', 'Максим', 'Сергеев', 34, 'Киев')
st_3 = Student('Developer', 'Ольга', 'Иванова', 29, 'Днепр')
st_4 = Student('Developer', 'Ирина', 'Никитова', 23, 'Бердянск')
st_5 = Student('Developer', 'Алексей', 'Олегов', 24, 'Харьков')
st_6 = Student('Developer', 'Роман', 'Дмитриев', 22, 'Николаев')
st_7 = Student('Developer', 'Максим', 'Анатолиев', 25, 'Денецк')
st_8 = Student('Developer', 'Дмитрий', 'Александров', 35, 'Мариуполь')
st_9 = Student('Developer', 'Алена', 'Павлова', 28, 'Ужгород')
st_10 = Student('Developer', 'Зоя', 'Никифорова', 21, 'Полтава')

gr_1 = Group('Курс ООП')
gr_1.add_student(st_1)
gr_1.add_student(st_2)
gr_1.add_student(st_3)
gr_1.add_student(st_4)
gr_1.add_student(st_5)
gr_1.add_student(st_6)
gr_1.add_student(st_7)
gr_1.add_student(st_8)
gr_1.add_student(st_9)
gr_1.add_student(st_10)

gr_1.delete_student(st_10)

gr_1.add_student(st_10)

print(gr_1.search_student('Никифорова'))
