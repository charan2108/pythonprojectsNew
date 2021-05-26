# Duck Typing Philosophy of Python

class Car:
    def start(self):
        print("MOdel is 360")
class Bike:
    def start(self):
        print("model is 60")        
def a(obj):
    obj.start()        

car = Car()
a(car)
bike = Bike()
a(bike)    

class Car:
    def model(self):
        print("WHts the car model")
    def mileage(self):
        print("the mileahe is")   
def b(obj):
    obj.model()
    obj.mileage()
car = Car() 
b(car)            