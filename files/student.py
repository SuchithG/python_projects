class Student:
    def __init__(self, id, name, testscore):
        self.id = id
        self.name = name
        self.testscore = testscore

    def display(self):
        print(self,self.name,self.testscore)