class Student():
    id = None
    name = None
    marks = None
    standard = 8

    def showStudent(self):
        #self (this) - it refers to current object
        print(self.id,self.name,self.marks,self.standard)

s_1 = Student()
s_1.id = 101
s_1.name = 'Ram'
s_1.marks = 87.54
s_1.showStudent()

s_2 = Student()
s_2.id = 102
s_2.name = 'Raman'
s_2.marks = 82.54
s_2.showStudent()
