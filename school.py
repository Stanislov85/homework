class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        # self.list_student = []
        self.gender = gender
        #self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        self.reduce_grade2 = 0
        if not isinstance(other, Student):
            return 'Второй объект не студент'
        else:
            return self.reduce_grade < other.reduce_grade  # сравнение средних оценок учеников

    def __str__(self):
        self.reduce_grade = 0
        grade_value_ob = []
        import statistics
        for (grade_key, grade_value) in self.grades.items():
           grade_value_ob += grade_value
           print(grade_value_ob)
        self.reduce_grade = statistics.mean(grade_value_ob)  # среднее значение
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя	оценка за домашние задания: {self.reduce_grade}  ' \
               f'\nКурсы в процессе изучения:{", ".join(self.courses_in_progress)}  ' \
               f'\nЗавершенные курсы: Введение	в программирование\n'

def Average_marks_students(list_students,course):
    midle = 0
    import statistics
    list_grades_student = []
    for student in list_students:
        if isinstance(student,Student):
            for (key,value) in student.grades.items():
                if key == course:
                    list_grades_student+= value
    midle = statistics.mean(list_grades_student)
    print(f'Средняя оценка по курсу {course} среди учеников: {midle}')


class Mentor:
    def __init__(self, name, surname) -> object:
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_Lecturers = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if not type(grade) == int and 0 <= grade <= 10:
            return print('Неправильная оценка')
        if not (isinstance(student,Student) and course in self.courses_attached and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        return 'Ошибка'

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname}\n'

class Lecturer(Mentor):
    def rate_Lecturer(self, lecturer, course, grade):
        if not (isinstance(lecturer, Lecturer) and course in self.courses_attached):
            if course in self.grades_Lecturers:
                self.grades_Lecturers[course] += [grade]
            else:
                self.grades_Lecturers[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.reduce_grade_1 = 0
        grade_Lecturers_value_ob = []
        import statistics
        for (grade_Lecturers_key, grade_Lecturers_value) in self.grades_Lecturers.items():
            grade_Lecturers_value_ob += grade_Lecturers_value
        self.reduce_grade_1 = statistics.mean(grade_Lecturers_value_ob)

        return f'Имя: {self.name} \nФамилия: {self.surname} ' \
               f'\nСредняя оценка за лекцию: {self.reduce_grade_1}\n '

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            return 'Второй объект отсутвует'
        else:
            return self.reduce_grade_1 < other.reduce_grade_1 # сравенеие средних оценок лекторов

def Average_marks_mentor(list_mentors,course):
    midle = 0
    import statistics
    list_grades_mentor = []
    for mentor in list_mentors:
        if isinstance(mentor,Mentor):
            for (key,value) in mentor.grades_Lecturers.items():
                if key == course:
                    list_grades_mentor += value
    midle = statistics.mean(list_grades_mentor)
    print(f'Средняя оценка по курсу {course} среди преподавателей: {midle}')

# ввод имени студентов
student1 = Student('Ruoy', 'Eman', 'man')
student2 = Student('Jeny', 'Vash', 'female')
student3 = Student('Ruoy1', 'Eman1', 'man1')
student4 = Student('Jeny1', 'Vash1', 'female1')

list_students = [student1,student2,student3,student4]

# ввод курса в процессе
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student3.courses_in_progress += ['Python']
student3.courses_in_progress += ['Git']
student4.courses_in_progress += ['Python']
student4.courses_in_progress += ['Git']



# ввод некого преподавателя
cool_mentor = Mentor('Some', 'Buddy')

# ввод курса который прилогается к преподавателю 
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

# ввод некого проверяющего
cool_Reviewer = Reviewer('Some', 'Buddy')

# ввод некого лекторам
cool_lecturer1 = Lecturer('Some', 'Buddy')
cool_lecturer2 = Lecturer('Peter', 'Ret')
cool_lecturer3 = Lecturer('Some1', 'Buddy1')
cool_lecturer4 = Lecturer('Peter1', 'Ret1')

list_mentors = [cool_lecturer1,cool_lecturer2,cool_lecturer3,cool_lecturer4]

# выставление оценок студенту1
cool_Reviewer.rate_hw(student1, 'Python', 3)
cool_Reviewer.rate_hw(student1, 'Python', 4)
cool_Reviewer.rate_hw(student1, 'Python', 5)
cool_Reviewer.rate_hw(student1, 'Git', 3)
cool_Reviewer.rate_hw(student1, 'Git', 4)
cool_Reviewer.rate_hw(student1, 'Git', 5)

# выставление оценок студенту2
cool_Reviewer.rate_hw(student2, 'Python', 2)
cool_Reviewer.rate_hw(student2, 'Python', 3)
cool_Reviewer.rate_hw(student2, 'Python', 4)
cool_Reviewer.rate_hw(student2, 'Git', 9)
cool_Reviewer.rate_hw(student2, 'Git', 9)
cool_Reviewer.rate_hw(student2, 'Git', 9)

# выставление оценок студенту3
cool_Reviewer.rate_hw(student3, 'Python', 1)
cool_Reviewer.rate_hw(student3, 'Python', 1)
cool_Reviewer.rate_hw(student3, 'Python', 1)
cool_Reviewer.rate_hw(student3, 'Git', 2)
cool_Reviewer.rate_hw(student3, 'Git', 2)
cool_Reviewer.rate_hw(student3, 'Git', 2)

# выставление оценок студенту4
cool_Reviewer.rate_hw(student4, 'Python', 3)
cool_Reviewer.rate_hw(student4, 'Python', 3)
cool_Reviewer.rate_hw(student4, 'Python', 3)
cool_Reviewer.rate_hw(student4, 'Git', 4)
cool_Reviewer.rate_hw(student4, 'Git', 4)
cool_Reviewer.rate_hw(student4, 'Git', 4)

# выставление оценок лектору1
cool_lecturer1.rate_Lecturer(cool_mentor, 'Python', 8)
cool_lecturer1.rate_Lecturer(cool_mentor, 'Python', 9)
cool_lecturer1.rate_Lecturer(cool_mentor, 'Python', 10)
cool_lecturer1.rate_Lecturer(cool_mentor, 'Git', 10)
cool_lecturer1.rate_Lecturer(cool_mentor, 'Git', 9)
cool_lecturer1.rate_Lecturer(cool_mentor, 'Git', 10)

# выставление оценок лектору2
cool_lecturer2.rate_Lecturer(cool_mentor, 'Python', 1)
cool_lecturer2.rate_Lecturer(cool_mentor, 'Python', 2)
cool_lecturer2.rate_Lecturer(cool_mentor, 'Python', 3)
cool_lecturer2.rate_Lecturer(cool_mentor, 'Git', 4)
cool_lecturer2.rate_Lecturer(cool_mentor, 'Git', 5)
cool_lecturer2.rate_Lecturer(cool_mentor, 'Git', 6)

# выставление оценок лектору3
cool_lecturer3.rate_Lecturer(cool_mentor, 'Python', 1)
cool_lecturer3.rate_Lecturer(cool_mentor, 'Python', 2)
cool_lecturer3.rate_Lecturer(cool_mentor, 'Python', 3)
cool_lecturer3.rate_Lecturer(cool_mentor, 'Git', 4)
cool_lecturer3.rate_Lecturer(cool_mentor, 'Git', 5)
cool_lecturer3.rate_Lecturer(cool_mentor, 'Git', 6)

# выставление оценок лектору4
cool_lecturer4.rate_Lecturer(cool_mentor, 'Python', 1)
cool_lecturer4.rate_Lecturer(cool_mentor, 'Python', 2)
cool_lecturer4.rate_Lecturer(cool_mentor, 'Python', 3)
cool_lecturer4.rate_Lecturer(cool_mentor, 'Git', 4)
cool_lecturer4.rate_Lecturer(cool_mentor, 'Git', 5)
cool_lecturer4.rate_Lecturer(cool_mentor, 'Git', 6)

print(student1.grades)
print(student2.grades)
print(student3.grades)
print(student4.grades)

print(cool_lecturer1.grades_Lecturers)
print(cool_lecturer2.grades_Lecturers)
print(cool_lecturer3.grades_Lecturers)
print(cool_lecturer4.grades_Lecturers)

some_Reviewer = cool_Reviewer
print(some_Reviewer)

some_student = student1
print(some_student)
some_student = student2
print(some_student)
some_student = student3
print(some_student)
some_student = student4
print(some_student)

some_lecturer = cool_lecturer1
print(some_lecturer)

some_lecturer = cool_lecturer2
print(some_lecturer)

some_lecturer = cool_lecturer3
print(some_lecturer)

some_lecturer = cool_lecturer4
print(some_lecturer)

Ruoy_Eman = student1
Jeny_Jeny = student2

print(f'Вывод сравнения оценок ученков: {Ruoy_Eman < Jeny_Jeny}')

Some_Buddy = cool_lecturer1
Peter_Ret = cool_lecturer2

print(f'Вывод сравнения оценок преподователей: {cool_lecturer1 > cool_lecturer2}')

Average_marks_students(list_students, 'Python')
Average_marks_students(list_students, 'Git')

Average_marks_mentor(list_mentors,'Python')
Average_marks_mentor(list_mentors,'Git')