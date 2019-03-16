class Vehicle():
    brand = 'Tata'

    def __init__(self,no_of_tyres, color, speed, price, type):
        self.data = []
        self.no_of_tyres = no_of_tyres
        self.color = color
        self.speed = speed
        self.price = price
        self.type = type

    def showVehicle(self):
        self.data.append([self.no_of_tyres, self.color, self.speed, self.price, self.type])
        print("Vehicle Details from : {}".format(Vehicle.brand))
        print(self.data)

    def __del__(self):
        print("Object Destroyed...")

obj_1 = Vehicle(4,'Red',300,'15L','Car')
obj_1.color = 'Yellow'
obj_1.showVehicle()
del obj_1
obj_2 = Vehicle(4,'Black',350,'18L','Car')
obj_2.showVehicle()