from abc import abstractmethod, ABC


class BMW(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod    # abstract method decorator  
    def drive(self):
        pass

class ThreeSeries(BMW):

    def __init__(self, curiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.curiseControlEnabled = curiseControlEnabled

    def display(self):
        print(self.curiseControlEnabled)

    def start(self):
        super().start() # Invoking parent class from child using super 
        print("Button start")

    def stop(self):
        super().stop() # Invoking parent class from child using super 
        print("Button start")
    

    def drive(self):
        print("Three series is being driven")

class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def start(self):
        super().start() # Invoking parent class from child using super 
        print("Remote start")

    def stop(self):
        super().stop() # Invoking parent class from child using super 
        print("Remote start")

    def drive(self):
        print("Five series is being driven")

bmw = ThreeSeries(True, "BMW", "328i", "2018")
print(bmw.curiseControlEnabled)
print(bmw.make)
print(bmw.model)
print(bmw.year)

bmw.start()
bmw.stop()
bmw.display()

fiveSeries = FiveSeries(True, "BMW", "328i", "2018")


