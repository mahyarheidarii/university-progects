class Student:
    def __init__(self, name, age, student_id, national_id, gpa):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.national_id = national_id
        self.gpa = gpa

    def reserve_food(self):
        print(f"{self.name} has reserved food.")

    def select_courses(self, courses):
        self.courses = courses
        print(f"{self.name} has selected the following courses: {', '.join(courses)}")


s1 = Student("Mahyar", 23, "01221040709011", "0025096583", 17.5)
s1.reserve_food()
s1.select_courses(["Math", "Physics", "Programming"])