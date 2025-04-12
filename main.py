class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_grade(self):
        grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(grades) / len(grades) if grades else 0
        
    def __str__(self):
        avg = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return  (f"Имя: {self.name}\n"
                 f"Фамилия: {self.surname}\n"
                 f"Средняя оценка за домашние задания: {round(avg + 0.01, 1)}\n"
                 f"Курсы в процессе изучения: {courses_in_progress}\n"
                 f"Завершенные курсы: {finished_courses}")
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented
    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(grades) / len(grades) if grades else 0    

    def __str__(self):
        avg = self.average_grade()
        return  (f"Имя: {self.name}\n"
                 f"Фамилия: {self.surname}\n"
                 f"Средняя оценка за лекции: {round(avg + 0.01, 1)}")
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return  (f"Имя: {self.name}\n"
                 f"Фамилия: {self.surname}")
        
# Новые данные для примера 

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']

another_lecturer = Lecturer('Jane', 'Smith')
another_lecturer.courses_attached += ['Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']

cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Git', 4)

best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 2)
best_student.rate_lecturer(another_lecturer, 'Git', 7)

print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)