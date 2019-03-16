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

    def __str__(self):
        # obj to string
        return str(self.data[0])

obj_1 = Vehicle(4,'Red',300,'15L','Car')
obj_1.color = 'Yellow'
obj_1.showVehicle()
print(obj_1)