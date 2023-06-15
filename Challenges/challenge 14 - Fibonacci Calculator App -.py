print("Welcome to the Fibonacci calculator app.")

nSequence = int(input("\nHow many digits of the Fibonacci sequence would you like to compute : "))

Fibonacci = [1 , 1]

print("\nThe first",nSequence,"numbers of the Fibonacci sequence are :")
print(Fibonacci[0])
print(Fibonacci[1])
for i in range(2 , nSequence):
    Fibonacci.append(Fibonacci[i - 2] + Fibonacci[i - 1])
    print(Fibonacci[i])

golden_ratio = [Fibonacci[i] / Fibonacci[i - 1] for i in range(1 , nSequence)]
print("\nThe corresponding values of Golden Ratio values are :")
for i in golden_ratio:
    print(i)
print("\nThe ratio of consecutive Fibonacci terms approaches the mathematical concept of PHI : 1.618...")