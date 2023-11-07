# invoking the instance using objects
class product:

    def __init__(self):
        self.name = 'IPhone'
        self.description = 'Its Awesome'
        self.price = 700

    def display(self):
        print(self.name)
        print(self.price) 
        print(self.description)

p1 = product()
p1.display() 



p2 = product()
p2.display()