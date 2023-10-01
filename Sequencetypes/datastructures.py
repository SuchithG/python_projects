students = {'John':['Python','Kernel','Java'], 'bob':['Python','Java'], 'jim':['JavaScript','React']}
keys = students.keys()
course = students.values()

for eachKey in keys:
    print('Courses taken by ',{eachKey}, 'are :')
    for eachCourse in students[eachKey]:
        print(eachCourse)
