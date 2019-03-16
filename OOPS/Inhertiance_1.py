class Bank():
    users = []
    def __init__(self):
        # self.users = []
        self._branch = 'Rohini'
        self._ifsc = 'ICIC010101'
        self._bank = 'ICICI'

class Account(Bank):

    def __init__(self, name, age, company, sal, acc_type, address):
        self.name = name
        self.age = age
        self.company = company
        self.sal = sal
        self.acc_type = acc_type
        self.address = address
        super().__init__()

    def show(self):
        print(self.name, self.age, self.company)
        print(self.acc_type, self.address)
        print("Branch", self._branch)
        print("IFSC", self._ifsc)
        print("Bank", self._bank)

obj_1 = Account('Ram', 25, 'HCL', 25000, 'Saving', 'Delhi')
# obj_1.storeData()
obj_1.show()

obj_2 = Account('Shyam', 27, 'HCL', 28000, 'Saving', 'Pune')
# obj_2.storeData()
obj_2.show()

# print(obj_1._ifsc)