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

user_1 = Facebook('Ram','ram@gmail.com','12345','cricket')
user_1.register()