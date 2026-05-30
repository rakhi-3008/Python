class Employee :
    start_time = "9am"
    end_time= "5pm"

class Teacher(Employee) :

    def __init__(self, subject) :
        self.subject = subject


t1 = Teacher("linear algebra")
print(t1.subject, t1.start_time, t1.end_time)


class Teachers :
    def __init__(self, salary):
        self.salary= salary

class Student :
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teachers, Student) :
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self,gpa)
        self.name=name

ta1 = TA(20000, 9.0, "rohit")