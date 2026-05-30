class Employee :
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee) :
    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()    #function overriding

class Doctor :
    def get_designation(self):
        print("designation = Doctor")

class Accountant :
    def get_designation(self):
        print("designation = Accountant")

d1 = Doctor()
d1.get_designation()

a1 =Accountant()
a1.get_designation()