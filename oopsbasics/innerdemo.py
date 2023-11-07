# Create a inner class

class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number