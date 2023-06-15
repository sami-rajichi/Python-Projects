name = input("Enter your name : ").title().strip()
print("Hello, " + name + "!")

print("\nI'll be converting your speed in miles per hour to meters per second")

speed_miles = float(input("What your speed in miles per hour? : "))
speed_meters = speed_miles * 0.4474
speed_meters = round(speed_meters, 2)
print("Dear " + name + " your speed in meters per second is " + str(speed_meters))