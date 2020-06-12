class Vehicle:
    licenseCode = ''
    face = ''
    serialCode = ''
    def TurnOnAirConditioner(self) :
        print('Turn On : Air')
class Car(Vehicle):
    def sayHello(self):
        print('HelloWorld')
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car()
car1.TurnOnAirConditioner()
car1.sayHello()

car2 = PickUp()
car2.TurnOnAirConditioner()

car3 = Van()
car3.TurnOnAirConditioner()

car4 = EstateCar()
car4.TurnOnAirConditioner()