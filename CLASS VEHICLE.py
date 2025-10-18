class Vehicle:
    def wheels(self):
        print("Vehicle has wheels.")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels.")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels.")

class Truck(Vehicle):
    def wheels(self):
        print("Truck has 6 wheels.")

# Test
vehicles = [Car(), Bike(), Truck()]
for v in vehicles:
    v.wheels()
