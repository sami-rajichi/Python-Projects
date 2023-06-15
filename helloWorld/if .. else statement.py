x = 100
y = 500

if x > y :
    print(x ," is greater than ", y)
elif x == y :
    print(x, " is equal to ", y)
else:
    print(x, " is smaller than ", y)

a = 100
b = 100

if a >= b : print(a)

print(a) if a > b else print("=") if a == b else print(b)