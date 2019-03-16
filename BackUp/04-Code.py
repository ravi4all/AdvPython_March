class Facebook():

    # constructor - used to initialize variables
    # when we create object it calls init by default
    def __init__(this, name,email,pwd,hobby):
        this.userData = []
        this.username = name
        this.useremail = email
        this.userpwd = pwd
        this.userhobby = hobby
    def register(this):
        this.userData.append([this.username, this.useremail, this.userpwd, this.userhobby])
        # print(this.username, this.useremail)
        print(this.userData)
    # destructor
    # delete will be called when program will terminate
    def __del__(self):
        print("Object Destroyed of",self.username)

user_1 = Facebook('Ram','ram@gmail.com','12345','cricket')
user_1.register()

del user_1

user_2 = Facebook('Raman','raman@gmail.com','15454','cricket')
user_2.register()

del user_2

user_3 = Facebook('Shyam','shyam@gmail.com','98988','cricket')
user_3.register()

try:
    print("Am I alive...",user_1.username)
except BaseException:
    print("No you are not...")