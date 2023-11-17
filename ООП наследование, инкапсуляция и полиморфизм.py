def average_rating(self): #Фуекция подсчёта средней оценки
        res = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return round(res, 2) #Округление до сотых

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #Завершённые курсы
        self.courses_in_progress = [] #Курсы в процессе 
        self.grades = {} #Оценки
        
    
    def rate_lecturer(self, lecturer, course, grade): #Метод оценки работы лектора
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print("Ошибка")
    
    def __str__(self):
        return f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n'f'Средняя оценка за домашние задания: {average_rating(self)}\n'f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'f'Завершенные курсы: {", ".join(self.finished_courses)}'
    
    def __lt__(self, other): #Метод сравнения по средней оценке
        if not isinstance(other, Student):
            return ('Объект не является классом Student')
        return average_rating(self) < average_rating(other)
            
        

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #Закреплённые за ментором курсы
        

        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) #Полная инициализация от родителя(Mentor)
        self.grades = {} #Словарь оценок от Student
    
    def __str__(self):
        return f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n'f'Средняя оценка за лекции: {average_rating(self)}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return ('Объект не является классом Lecturer')
        return average_rating(self) < average_rating(other)    
    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) #Полная инициализация от родителя(Mentor)
    
    def rate_hw(self, student, course, grade): #Функция проверки д.з.
        if isinstance(student, Student) and (course in self.courses_attached) and (course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя : {self.name}\n'f'Фамилия : {self.surname}'

    
#Студенты:
student_1 = Student('Иван', 'Митрохин', 'МУЖ')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['PHP']

student_2 = Student('Ифраим', 'Диверолли', 'МУЖ')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Python']

student_3 = Student('Алина', 'Царева', 'ЖЕН' )
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['PHP']
#Лекторы:
lecturer_1 = Lecturer('Олег', 'Крикет')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Артем', 'Франиз')
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Екатерина', 'Фортуна')
lecturer_3.courses_attached += ['Python']



#Проверяющие:
reviewer_1 = Reviewer('Виктория', 'Одинцова')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Татьяна', 'Сидорова')
reviewer_2.courses_attached += ['Java']
#Менторы
mentor_1 = Mentor('Анна', 'Питушкина')
mentor_2 = Mentor('Сергей', 'Антоно')

#Проверка методов:
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Java', 9)
student_1.rate_lecturer(lecturer_3, 'Python', 5)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_1.rate_hw(student_3, 'Python', 6)

print(student_1, '\n') #Метод __str__
print(student_2, '\n') #Метод __str__
print(reviewer_1, '\n') #Метод __str__
print(reviewer_2, '\n') #Метод __str__
print(lecturer_1, '\n') #Метод __str__
print(lecturer_2, '\n') #Метод __str__
print(student_1 > student_2) #Метод __lt__
print(lecturer_1 > lecturer_2) #Метод __lt__

print()
print()

#Функции подсчета средней оценки по всем студентам/лекторам в рамках конкретного курса
student_list = [student_1, student_3]
lecturer_list = [lecturer_1, lecturer_3]

def average_grade_student(list, course):
    count = 0 #Сумма всех оценко
    countlen = 0 #Количество всех оценок студентов
    for student in list:
        countlen += len(student.grades[course])
        for grade in student.grades[course]:
            count += grade
    return round(count / countlen, 2)

def average_grade_lecturer(list, course):
    count = 0
    countlen = 0
    for lecturer in list:
        countlen += len(lecturer.grades[course])
        for grade in lecturer.grades[course]:
            count += grade
    return round(count / countlen, 2)

#Проверка
print(average_grade_student(student_list, 'Python'))
print(average_grade_lecturer(lecturer_list, 'Python'))



