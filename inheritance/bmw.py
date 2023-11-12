class BMW:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ThreeSeries:

    def __init__(self, curiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.curiseControlEnabled = curiseControlEnabled

class FiveSeries:

    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
print(threeSeries.curiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
        

