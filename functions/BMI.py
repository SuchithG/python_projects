#bmi = weight in kg/(height in meters)

def calaculateBMI(height, weight):
    heightInMeters = height * 0.4536
    bmi = weight / (heightInMeters * heightInMeters) # height in meters squared
    return bmi

print(calaculateBMI(5.9,78.5))
