# parent class
class vehicle(object):

    # __init__ is known as the constructor
    def __init__(self, colour, price,max_speed):
        print("constructor of parent class will involed when a object of created of child class")
        self.colour = colour
        self.price = price
        self.max_speed = max_speed

    def display(self):
        print(self.colour)
        print(self.price)
        print(self.max_speed)
# child class
class car(vehicle):
    def __init__(self,colour,price,max_speed, numberofTyre):
        # __init__ is known as the constructor
        print("child class constructor will be invoked when child class object is created")
        #invloking the constructor of parent class
        self.numberofTyre = numberofTyre
        vehicle.__init__(self, colour, price, max_speed)

    def show(self):
        print("A" , self.colour , "-coloured car with the maximum speed of " , self.max_speed , "km/h is priced at " , self.price , "with " , self.numberofTyre , "tyres."  )

a = car( 'red', 500000, 200, 4 )

a.show() # displaying the desired result

