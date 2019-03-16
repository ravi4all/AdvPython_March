class Bank():
    # users = []
    def __init__(self, name, age, company, sal):
        self.users = []
        self.name = name
        self.age = age
        self.company = company
        self.sal = sal

    def storeData(self):
        self.users.append([self.name, self.age, self.company, self.sal])

class Account():

    def __init__(self, acc_type, address):
        self.acc_type = acc_type
        self.address = address

    def show(self):
        print(self.acc_type, self.address)

class Loan(Bank,Account):

    def __init__(self,name, age, company, sal, acc_type, address):
        super().__init__(name, age, company, sal)
        Account.__init__(self,acc_type, address)

    def checkSalary(self):
        for i in range(len(self.users)):
            if self.users[i][-1] > 25000:
                print("Loan Approved to", self.users[i][0])
            else:
                print("Loan Not Approved to", self.users[i][0])
    # Override
    def show(self):
        print(self.users)

# obj_1 = Account('Ram', 25, 'HCL', 25000, 'Saving', 'Delhi')
# obj_1.storeData()
# obj_1.show()
#
# obj_2 = Account('Shyam', 27, 'HCL', 28000, 'Saving', 'Pune')
# obj_2.storeData()
# obj_2.show()

obj_1 = Loan('Ram', 25, 'HCL', 25000, 'Saving', 'Delhi')
obj_1.storeData()
obj_1.show()
obj_1.checkSalary()

obj_2 = Loan('Shyam', 27, 'HCL', 28000, 'Saving', 'Pune')
obj_2.storeData()
obj_2.show()
obj_2.checkSalary()