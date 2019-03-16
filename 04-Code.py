class Student():
    def __init__(self,ID,Name,Age):
        self.ID = ID
        self.Name = Name
        self.Age = Age
        self.data = []

    def menu(self):
        print("""1. create student
2. update student
3.delete student""")
        ch = input("enter your choice:")
        todo = { "1" : self.createStudent,
                 "2" : self.updateStudent,
                 "3" : self.deleteStudent}
        

    def createStudent(self,ID,Name,Age):
        print("enter ID,Name,Age")
        self.apend.data([self.ID,self.Name,self.Age])

    def updateStudent(self):
        print("enetr ID to be updated")
        if self.ID in self.data:
            del self.data[self.ID,self.Name,self.Age]
            
            self.apend.data
        else :
            print("wrong ID")
        

    def deleteStudent(self):
        pass

obj = Student()
obj.menu()
