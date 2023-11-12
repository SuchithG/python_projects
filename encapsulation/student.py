class Student:
    def __init__(self):
        self.__id = 123 # private
        self.__name = "John"

    def display(self):
        print(self.__id)
        print(self.__name)

s = Student()
print(s._Student__id) # Name mangling