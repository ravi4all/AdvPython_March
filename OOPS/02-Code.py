class Vehicle():
    brand = 'Tata'
    data = []
    def showVehicle(self, no_of_tyres, color, speed, price, type):
        self.data.append([no_of_tyres, color, speed, price, type])
        print("Vehicle Details from : {}".format(Vehicle.brand))
        print(self.data)

obj_1 = Vehicle()
obj_1.showVehicle(4,'Red',300,'15L','Car')

obj_2 = Vehicle()
obj_2.showVehicle(4,'Black',350,'18L','Car')

obj_3 = Vehicle()
obj_3.showVehicle(4,'Orange',250,'8L','Car')