class BMW:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

class ThreeSeries(BMW):

    def __init__(self, curiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.curiseControlEnabled = curiseControlEnabled

    def display(self):
        print(self.curiseControlEnabled)

    def start(self):
        print("Button start")

class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
print(threeSeries.curiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()


