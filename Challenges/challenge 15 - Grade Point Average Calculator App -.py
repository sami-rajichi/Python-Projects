print("Welcome to the grade point average calculator app.\n")

name = input("What's your name : ").title().strip()

nbOfGrades = int(input("How many grades would you like to enter : "))
grades = [float(input("Enter grade : ")) for i in range(nbOfGrades)]

print("\ngrades from highest to lowest :")
grades.sort(reverse=True)
for i in grades:
    print("\t\t",i)

print("\n*** "+name+"'s grades summary ***")
print("\t\tTotal number of grades : ", len(grades))
print("\t\tHighest grade : ",grades[0])
print("\t\tLowest grade : ",grades[len(grades) - 1])
print("\t\tAverage : ", round(sum(grades) / len(grades), 2))

desired_nb = float(input("\nWhat's your desired average : "))

print("\nGood luck "+ name)
print("You'll need to get", (desired_nb * (len(grades) + 1)) - sum(grades),"on your next assignment to earn", desired_nb,"average.")

print("Let's see what your average could have been if you did better/worse on an assignment.")
changedGrade = float(input("What grade would you like to change : "))
newGrade = float(input("What grade would you like to change "+str(changedGrade)+" to : "))
newGrades = grades.copy()
newGrades.remove(changedGrade)
newGrades.append(newGrade)

print("\nNew grades from highest to lowest :")
newGrades.sort(reverse=True)
for i in newGrades:
    print("\t\t",i)

print("\n*** "+name+"'s new grade summary ***")
print("\t\tTotal number of grades : ", len(newGrades))
print("\t\tHighest grade : ",max(newGrades))
print("\t\tLowest grade : ",min(newGrades))
print("\t\tAverage : ", round(sum(newGrades) / len(newGrades), 2))

print("\nYour new average would be", round(sum(newGrades) / len(newGrades) , 2),"compared to the real one",round(sum(grades) / len(grades) , 2))
print("There's a change of", round(sum(newGrades) / len(newGrades) , 2) - round(sum(grades) / len(grades) , 2))

print("\nToo bad your original grades are still the same!")
print(grades)
print("You should go to ask for extra credit!")