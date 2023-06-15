import cmath

print("Welcome to the quadratic equation solver app\n")

print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers")
print("A complex number has two parts : a + bj")
print("Where a is the real portion and bj is the imaginary portion.\n")

numberOfEquation = int(input("How many equations do you want to solve :"))

for i in range(1,numberOfEquation+1):
    print("\nSolving equation #"+str(i))
    print('-------------------------------------------------------------------\n')
    va = float(input("Enter the value of a ( coefficient of x^2 ) : "))
    vb = float(input("Enter the value of b ( coefficient of x ) : "))
    vc = float(input("Enter the value of c ( coefficient of c ) : "))
    print("The solutions to "+str(va)+"x^2 + "+str(vb)+"x + "+str(vc)+" = 0 are :\n")
    print("\t\tx1 =",(-vb - cmath.sqrt(vb ** 2 - (4 * va * vc))) / 2 * va)
    print("\t\tx2 =", (-vb + cmath.sqrt(vb ** 2 - (4 * va * vc))) / 2 * va)
print("\nThank you for using quadratic equation solver app, Goodbye.")