import math

name = input("Enter your name : ").title().strip()
print("Hello, " + name)

print("This program is responsible for calculating the Hypotenus and the area of a Triangle.")

triangle_leg1 = float(input("Enter the first leg of the triangle : "))
triangle_leg2 = float(input("Enter the second leg of the triangle : "))

hypo = round(math.sqrt(triangle_leg1 ** 2 + triangle_leg2 ** 2), 3)

area = round(0.5 * triangle_leg2 * triangle_leg1, 3)

print("For the triangle of leg = " + str(triangle_leg1) + " and leg = " + str(triangle_leg2) + " the hupotenus is " + str(hypo))
print("For the triangle of leg = " + str(triangle_leg1) + " and leg = " + str(triangle_leg2) + " the area is " + str(area))