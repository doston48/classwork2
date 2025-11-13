class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        if self.grade >= 50:
            return "Pass"
        else:
            return "Fail"
        
s1 = Student("bob", 75)
s2 = Student("jhon", 45)

print(s1.name, s1.is_passing())
print(s2.name, s2.is_passing()) 