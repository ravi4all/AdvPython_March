import sys
sys.path.append('..')
from model import model

def addEmp(name,id,pwd,dept):
    # print(name, id, pwd, dept)
    empList = model.addEmp(name,id,pwd,dept)
    return empList

def readEmp():
    pass

def deleteEmp(emp_id):
    model.deleteEmp(emp_id)