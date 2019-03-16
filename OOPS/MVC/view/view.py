import sys
sys.path.append('..')
from controller import controller

def addEmp():
    emp_name = input("Enter your name : ")
    emp_id = input("Enter your ID : ")
    emp_pwd = input("Enter your password : ")
    emp_dept = input("Enter your dept : ")

    empList = controller.addEmp(emp_name, emp_id, emp_pwd, emp_dept)
    # print(empList)
    for emp in empList:
        print(emp)

def readEmp():
    pass

def updateEmp():
    pass

def deleteEmp():
    emp_id = input("Enter EmpID : ")
    controller.deleteEmp(emp_id)

def searchEmp():
    pass

def errHandler():
    print("Invalid Choice...")

while True:
    print("""
    1. Add Emp
    2. Read Emp
    3. Update Emp
    4. Delete Emp
    5. Search Emp
    """)

    userChoice = input("Enter your choice : ")
    operations = {
        "1":addEmp,
        "2":readEmp,
        "3":updateEmp,
        "4":deleteEmp,
        "5":searchEmp
    }
    operations.get(userChoice)()