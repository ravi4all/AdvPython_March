class Emp:
    # Protected
    _emp_id = 101
    # Private
    __emp_name = "Ram"
    __emp_sal = 25000
    __emp_dept = 'IT'

    def show(self):
        print(self._emp_id,self.__emp_name,self.__emp_dept,self.__emp_sal)

obj = Emp()
# obj.__emp_name = 'Shyam'
# print(obj._emp_id)
obj.show()