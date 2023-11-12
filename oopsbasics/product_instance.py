# invoking the instance using objects
class product:

    def __init__(self):
        self.name = 'IPhone'
        self.description = 'Its Awesome'
        self.price = 700

    def __del__(self):
        print("Inside the destructor")

    def display(self):
        print(self.name)
        print(self.price) 
        print(self.description)

p1 = product()
p1.display() 
p1 = None # Tells the gc no more reference to the object


p2 = product()
p2.display()
p2 = None