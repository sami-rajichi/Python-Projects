# Lambda functions are anonymous functions that are only used for a short period of time and they are used in one line
# Lambda functions require only arguments

x = lambda a : a * 10
print(x(50))

y = lambda a , b , c : (a + b) * (b - c)
print(y(100 , 50 , 20))

def first_function(n):
    return lambda p : p * n
s = first_function(5)
print(s(100))