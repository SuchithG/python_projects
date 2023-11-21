# Driving license checker using Exceptions

class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg

class TooOldException(Exception):
    def __init__(self, msg):
        self.msg = msg

age = int(input('enter the age'))
if age < 18 :
    raise TooYoungException("You have to be 18 or older to apply.")
elif age > 90 :
    raise TooOldException("You have to be younger than 90 to apply.")
else :
    print("You are eligible to apply for license!")