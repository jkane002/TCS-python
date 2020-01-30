'''
Suppose we are writing code to track different types of cars in a race. There
are three types of cars, a sports car, a van, and a truck. For one move, a
sports car moves 5 units forward, a van 3, and a truck 1. Each move uses
one unit of gas; and a sports car starts with 10 gallons, and van with 15 and
a truck with 25. Write some code using factory methods that tracks the gas and units
travelled of each vehicle.

Constraints
Assume you will never go into negative gas
'''
class Car():
    def factory(type):
        if (type =="Van"):
            return Van()
        if (type =="SportsCar"):
            return SportsCar()
        if (type =="Truck"):
            return Truck()
        assert 0, "Bad Car creation: " + type

class SportsCar(Car):
    def __init__(self):
        self.location = 0
        self.gas = 10
    def move(self):
        self.location = self.location + 5
        self.gas = self.gas - 1
        print ("Sports car at ", self.location , " with ", self.gas, "gallon(s) of gas")

class Van(Car):
    def  __init__(self):
        self.location = 0
        self.gas = 15
    def move(self):
        self.location = self.location + 3
        self.gas = self.gas - 1
        print("Van at ", self.location ," with ", self.gas, "gallon(s) of gas")

class Truck(Car):
    def __init__(self):
        self.location = 0
        self.gas = 25
    def move(self):
        self.location = self.location + 1
        self.gas = self.gas - 1
        print ("Truck at ", self.location , " with ", self.gas, "gallon(s) of gas")

van = Car.factory('Van')
van.move()
sc = Car.factory('SportsCar')
sc.move()
truck = Car.factory('Truck')
truck.move()
