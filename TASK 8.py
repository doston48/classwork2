class Student:
    def __init__(self, name, grades):
   
    
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
 
    
        self.grades.append(grade)
        print(f"Added grade {grade} for {self.name}")

    def average(self):
        average = sum(self.grades) / len(self.grades)
        print(f"The average grade for {self.name} is {average}")

student1 = Student("Alice", [90, 10, 50, 40])
student2 = Student("Bob", [80, 85, 70, 90])

student1.add_grade(100)


student1.average()
student2.average()


if (sum(student1.grades) / len(student1.grades)) > (sum(student2.grades) / len(student2.grades)):
    print(f"{student1.name} has a higher average.")
else:
    print(f"{student2.name} has a higher average.")