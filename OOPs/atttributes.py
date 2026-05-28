class Student :
    college_name = "ABC college"    #class attributes

    def __init__(self, name, rollno, age):
        self.name = name,       #instance attributes
        self.rollno = rollno,
        self.age = age


stu1 = Student("rakhi", 81, 21)
print(stu1.name, stu1.rollno, stu1.age, stu1.college_name)