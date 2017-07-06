"""
Charachters project for coding dojo
"""
# pylint: disable=c0103
class Bike(object):
    #we define a cl;ass and indicate the paramenters as an object
    def __init__(self, price, max_speed):
        #customizing a function with the magic method that initializes the attritubes of the object
        self.price = price
        #self.price is the pointer to the memory location to the object price
        self.max_speed = max_speed
        #self.max_speed is the pointer to the memory location to the object max_price
        self.miles = 0
        #self.miles is the pointer to the memory location to the object miles.
        #self.miles is establishing a default value of 0.  self.miles does not
        #need a parameter because it is set.
    def displayInfo(self):
        #displayInfo is in camel case with a capital I in "info"
        #any method that lives inside the class needs access to the particular instance,
        #which is the object
        print self.price
        print self.max_speed
        print self.miles
        return self
        #returning self allows the information to be accessed at a later time
        #it also creates the opportunity to check your code

    def ride(self):
        print "riding"
        self.miles += 10
        #adds 10 miles to elf.miles total
        return self

    def reverse(self):
        print "reversing"
        self.miles -= 5
        #subtracts 5 miles from mile total
        if self.miles < 0:
        #if self.miles becomes less than 0
            self.miles = 0
            #self.miles becomes 0, we do not want negative miles
        return self
bike1 = Bike(200, "25mph")
#the 200 integer represents the price that will be passed in
#the "25mph" string represents the max_speed that will be passed in
#note:that no miles are needed here because we have a set value for miles in
#__init__
bike2 = Bike(500, "7mph")
bike3 = Bike(150, "40mph")
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
# 3 test cases
