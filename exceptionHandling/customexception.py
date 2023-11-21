# Create and Raise Custom Exceptions

class overTheLimitException(Exception):
    def __init__(self, msg):
        self.msg = msg # adding msg to the constructor

def withdrawl(amount):
    if(amount > 500):
        raise overTheLimitException("You cannot withdraw more than 500$ per day")
    
withdrawl(600)