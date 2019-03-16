class Vehicle():
    no_of_tyres = None
    color = None
    speed = None
    price = None
    type = None
    brand = 'Tata'

    def showVehicle(self):
        print("Vehicle Details from : {}".format(Vehicle.brand))
        print("""
        Number of tyres : {}
        Color : {}
        Speed : {}
        Price : {}
        type : {}
        """.format(self.no_of_tyres, self.color, self.speed, self.price, self.type))

obj_1 = Vehicle()
obj_1.no_of_tyres = 4
obj_1.speed = 400
obj_1.type = 'Car'
obj_1.price = '12L'
obj_1.color = 'black'
obj_1.showVehicle()

obj_2 = Vehicle()
obj_2.no_of_tyres = 4
obj_2.speed = 300
obj_2.type = 'Car'
obj_2.price = '15L'
obj_2.color = 'red'
obj_2.showVehicle()