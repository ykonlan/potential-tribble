class Student:
    def __init__(self,name,age,grade = None):
        self.name = name
        self.age = age
        self.grade = grade if grade is not None else []

    def display_info(self):
        if self.grade:
            return f"Name: {self.name}\nAge:{self.age}\nGrade:{self.grade}\nAverage Grade:{self.grade_average():.2f}"
        else:
            return f"Name: {self.name}\nAge:{self.age}"

    def grade_average(self):
        if self.grade:
            return sum(self.grade)/len(self.grade)
        else:
            return 0
        
    def add_grade(self):
        marks = list(map(int,input("Enter the marks you'd like to append, rounded to the nearest whole number and separated with space").split()))
        valid_marks = [mark for mark in marks if 0<=mark <= 100]
        invalid_marks = [mark for mark in marks if 0 > mark or mark > 100]
        if valid_marks:
            self.grade.extend(valid_marks)
            print(f"Marks recorded: {' '.join(map(str,valid_marks))}")
        if invalid_marks:
            print(f"Invalid Marks: {' '.join(map(str,invalid_marks))}")
        return "Grades uploaded!"
               


student1 = Student("Stephan", 19, [81, 72, 90])

print(student1.display_info())  # Before adding grades

student1.add_grade()  # Adds grades

print(student1.display_info())  # Should reflect the new grades



       