class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
   
    def displayhealth(self):
        print 'health =' + str(self.health)
        return self
    
    def walk(self, health):
        self.health -= 1
        return self
    
    def run(self, health):
        self.health -= 5
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
        
    def pet(self, health):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return self
   
    def displayhealth(self):
        print "I am a Dragon"
        super(Dragon, self).displayhealth()

class Bear(Animal):
    def __init__(self, name):
        super(Bear, self).__init__(name)
        self.health = 160

animal1 = Dog('woof')
animal1.walk().walk().walk().run().run().pet().displayhealth()
animal2 = Dragon('roar')
animal2.fly().displayhealth()
animal3 = Dog('bark')
animal3.fly()
animal4 = Bear('growl')
animal4.displayhealth()
animal5 = Bear('growler')
animal5.pet().displayhealth()
animal6 = Bear('growling')
animal6.fly.displayhealth()
animal1.displayhealth()
animal2.displayhealth()
animal3.displayhealth()
animal4.displayhealth()
animal5.displayhealth()
animal6.displayhealth()
