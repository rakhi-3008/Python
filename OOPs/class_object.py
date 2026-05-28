class Student :
    def __init__(self, name, cgpa):
        self.name = name 
        self.cgpa = cgpa
        print("this is constructor", name)

    def get_cgpa(self):
        return self.cgpa


stu1 = Student("rakhi", 9.9)
print(stu1.get_cgpa())
