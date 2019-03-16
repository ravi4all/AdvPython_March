class Emp():

    def __init__(self, name, id, pwd, dept):
        self.name = name
        self.id = id
        self.pwd = pwd
        self.dept = dept
        self.branch = 'Delhi'

    def __str__(self):
        return self.name + "," + self.id + "," + self.pwd + "," + self.dept

empList = []
def addEmp(name,id,pwd,dept):
    emp = Emp(name,id,pwd,dept)
    empList.append(emp)
    # print(empList)
    # print("Emp added successfully...")
    return empList

def deleteEmp(emp_id):
    for i in range(len(empList)):
        if emp_id == empList[i].id:
            # print("You want to delete",emp.name)
            del empList[i]