class HDFCBank():
    username = None
    userage = None
    userAccType = None
    userPin = None
    userBranch = 'Rohini'

customer_1 = HDFCBank()
customer_1.username = 'Ram'
customer_1.userage = 30
customer_1.userAccType = 'Saving'
customer_1.userPin = 1234
# print(customer_1)
print(customer_1.username, customer_1.userAccType)