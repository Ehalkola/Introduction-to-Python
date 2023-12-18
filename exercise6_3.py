# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application')

avg = 0
grades = 0
students = int(input("Input the amount of students (1-5): "))

number = students + 1

for students in range(1, number):
    print("Input students grade")
    grade = float(input("Input students grade: "))
    grades += grade
avg = round((grades / students), 3)
print(avg)

if 0 <= avg <= 1:
    print("Bad result")
elif 1 <= avg <= 2:
    print("Weak result")
elif 2 <= avg <= 3:
    print("Average result")
elif 3 <= avg <= 4:
    print("Good result")
elif 4 <= avg <= 5:
    print("Excellent result!")
# Welcome the user to the application and tell them what it's for
print('Hello! Welcome to use our application')
