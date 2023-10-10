"""
maths_marks = float(input("Enter the marks in maths: "))
physics_marks = float(input("Enter the marks in physics: "))
chemistry_marks = float(input("Enter the marks in chemistry: "))

total_marks = maths_marks + physics_marks + chemistry_marks

average = total_marks / 3

if total_marks <= 59 :
    print(f"Average marks:{average:.2f}", "Grade C")
elif total_marks <= 69 :
    print(f"Average marks:{average:.2f}", "Grade B")
elif total_marks <=79:
    print(f"Average marks:{average:.2f}", "Grade A")
elif total_marks <= 35:
    print("Student has failed")
"""

total_marks = [float(x) for x in input("Enter the marks in three subjects with a space each: ").split()]
Final_marks = sum(total_marks)
average = Final_marks/3

if Final_marks <= 59 :
    print(f"Average marks:{average:.2f}", "Grade C")
elif Final_marks <= 69 :
    print(f"Average marks:{average:.2f}", "Grade B")
elif Final_marks <=79:
    print(f"Average marks:{average:.2f}", "Grade A")
elif Final_marks <= 35:
    print("Student has failed")

