class Student:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average = 0

    def avg(self, score, lectures):
        self.average = score/lectures
        return self.average

student_1 = Student(first_name="Taras", second_name="Shevchenko", age=18)
student_2 = Student(first_name="Lesya", second_name="Ukrainka", age=17)
student_3 = Student(first_name="Hrihory", second_name="Skovoroda", age=21)

print(student_1.avg(80, 10))
print(student_2.avg(90, 15))
print(student_3.avg(100, 20))