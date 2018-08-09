class Pet:
    '''__init__() is a method of the class Pet
    .A method is a function that belongs to a class instance. All methods of a class first parameter is self'''
    def __init__(self,name,age,animal="dog"):
        '''self.name and self.age are instance attributes or data members of the class Pet. Instance attributes are unique in every occurance (instance) of a Pet object'''
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hunger = False
        self.mood = "Happy"

    def eat (self):
        self.is_hunger = False

    def __str__(self):
        return "{0} {1}".format(self,name,age,animal)

'''The pet class has the members age,name,count,__init()__self. To call the __init__() function we use the class name with the respective parameters within parenthesis'''

def madeHunger(pet):
    pet.is_hunger = True

#o is an object of Pet
o = Pet("Dog", 3)

#t is another object of Pet
t = Pet("Cat", 4)
print "Before call to makeHunger()"
print o.name, o.age, o.count
print t.name, t.age, t.count

makeHunger(o)

print "After call to makeHunger() and before call to eat()"
print o.name, o.age, o.count
print t.name, t.age, t.count

o.eat
print o.name, o.age, o.count
print t.name, t.age, t.count
