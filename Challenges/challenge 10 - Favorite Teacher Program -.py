import random

print("*** Welcome to favorite teacher program ***\n")

t = []
numberOfTeacher = int(input("How many favorite teachers you want to mention :"))
for i in range(0,numberOfTeacher):
    print("Who is your",i+1,"favorite teacher : ",end="")
    name = input().title().strip()
    t.append(name)

print("Your favorite ranked teachers are", t)
print("Your favorite ranked teachers sorted alphabetically are", sorted(t))
print("Your favorite ranked teachers sorted in reverse order are", sorted(t, reverse=True))

print("\nYour top two teachers are",t[0:2])
print("Your next favorite teachers are",t[2:])
print("Your last favorite teacher is",t[len(t)-1])
print("You have a total",len(t),"of favorite teachers.")

ranNum = random.randint(0,numberOfTeacher-1)

print("\nOops,",t[0],"is no longer your first favorite teacher. ",end='')
t.insert(0, input("So who'd be your top favorite teacher : ").title().strip())

print("\nYour favorite ranked teachers are", t)
print("Your favorite ranked teachers sorted alphabetically are", sorted(t))
print("Your favorite ranked teachers sorted in reverse order are", sorted(t, reverse=True))

print("\nYour top two teachers are",t[0:2])
print("Your next favorite teachers are",t[2:])
print("Your last favorite teacher is",t[len(t)-1])
print("You have a total",len(t),"of favorite teachers.")

print("You've decided you no longer like a teacher, which teacher do you want to remove from your list :",t[ranNum])
t.remove(t[ranNum])

print("\nYour favorite ranked teachers are", t)
print("Your favorite ranked teachers sorted alphabetically are", sorted(t))
print("Your favorite ranked teachers sorted in reverse order are", sorted(t, reverse=True))

print("\nYour top two teachers are",t[0:2])
print("Your next favorite teachers are",t[2:])
print("Your last favorite teacher is",t[len(t)-1])
print("You have a total",len(t),"of favorite teachers.")