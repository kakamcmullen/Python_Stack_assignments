"""
Charachters project for coding dojo
"""
# pylint: disable=c0103
class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if self.price > 10000:
            self.tax = 15
        else:
            self.tax = 12

    def display_all(self):
        print self.price
        print self.speed
        print self.fuel
        print self.milage
        print self.tax
        return self

Car1 = Car(15000, "160 mph", "full", "12 mpg")
Car2 = Car(22000, "100 mph", "half", "8 mpg")
Car3 = Car(50000, "120 mph", "quarter", "16 mpg")
Car4 = Car(8000, "70 mph", "empty", "16 mpg")
Car5 = Car(500, "85 MPH", "NONE", "20 mpg")
Car6 = Car(200000, "230 mph", "full", "32 mpg")
Car1.display_all()
Car2.display_all()
Car3.display_all()
Car4.display_all()
Car5.display_all()
Car6.display_all()
