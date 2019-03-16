class Student():
    id = None
    name = None
    marks = None
    standard = 8
    data = []

    def showStudent(self,id,name,marks):
        self.data.append([id,name,marks,self.standard])
        print(self.data)

s_1 = Student()
s_1.standard = 9
s_1.showStudent(101,'Ram',78.6)

s_2 = Student()
s_2.showStudent(102,'Raman',86.5)
