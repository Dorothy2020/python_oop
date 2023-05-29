class Student:
    def __init__(self,name,age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self,student):
        if len(self.students)<self.max_students:
            self.students.append (student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.grade
        return value / len(self.students)

S1 = Student("Alexo",16,80)
S2 = Student("Sandy",17,90)
S3 = Student("Bancy",20,95)

course = Course("Math",2)
course.add_student(S1)
course.add_student(S2)

print(course.students [1].name)
print(course.get_average_grade())





