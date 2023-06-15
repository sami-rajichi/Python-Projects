import datetime

grocery_store = ['meat'.title().strip(), 'chEese'.title().strip()]
print("Welcome to Grocery shopping app")
time = datetime.datetime.now()
print("the current date and time is",time.day,"/",time.month,"/",time.year,"  ",time.hour,":",time.minute)
print("you currently have",grocery_store[:len(grocery_store)-1],"and ['"+grocery_store[len(grocery_store)-1]+"']")

for x in range(1,4):
    grocery_store.append(input("Add a new food to the grocery list:").title().strip())
print("Here is your grocery list :",end=" ")
print(grocery_store)

grocery_store.sort()
print("Here is your grocery list sorted :",end=" ")
print(grocery_store)

print("\nSimulating grocery shopping...\n")
for i in range(1,4):
    print("Current grocery list contains",len(grocery_store),"which are :",grocery_store[:])
    purchased_food = input("What did you just buy :").title().strip()
    grocery_store.remove(purchased_food)
    print("Removing",purchased_food,"from list...\n")

print("Current grocery list contains",len(grocery_store),"which are :",grocery_store[:])
print("Sorry the store is out of",grocery_store[len(grocery_store)-1])
grocery_store[len(grocery_store)-1] = input("What food would you like instead :").title().strip()
print("Her what remains on your grocery list :",sorted(grocery_store))