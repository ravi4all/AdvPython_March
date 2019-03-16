class Student():

    # constructor
    # it is called whenever we create object
    def __init__(self,id,name,marks):
        self.id = id
        self.name = name
        self.marks = marks
        self.standard = 8
        self.data = []

    def showStudent(self):
        #self.data.append([id,name,marks,self.standard])
        #print(self.data)
        self.data.append([self.id, self.name, self.marks, self.standard])
        print(self.data)

s_1 = Student(101,'Ram',78.6)
s_1.standard = 9
s_1.showStudent()

s_2 = Student(102,'Raman',86.5)
s_2.showStudent()
