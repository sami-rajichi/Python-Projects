name = input("Enter your name : ").title().strip()
print("Hello, " + name)

print("Welcome to grades sorter application \n")

grades = []
grades.append(float(input("Enter your first grade [0..20] : ")))
grades.append(float(input("Enter your second grade [0..20] : ")))
grades.append(float(input("Enter your third grade [0..20] : ")))
grades.append(float(input("Enter your fourth grade [0..20] : ")))

print("your grades are : ", grades)

grades.sort(reverse=True)

print("your grades from highest to lowest are : ", grades)

print("\n Now your lowest grades will be dropped..")

rem_grade1 = grades.pop()
rem_grade2 = grades.pop()

print("Your first lowest grade is " + str(round(rem_grade1)))
print("Your second lowest grade is " + str(round(rem_grade2)))

print("\nYour remaining grades are : ", grades)
print("nice work! your highest grade is " + str(round(grades[0], 2)))