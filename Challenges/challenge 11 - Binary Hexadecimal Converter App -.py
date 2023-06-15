print("Welcome to the binary/hexadecimal converter app")

print("\nCompute binary and hexadecimal values up to the following decimal number : ",end='')
fNb = int(input())
print("Generating lists ... Complete!")

decimal_number = list(range(1, fNb+1))
binary_number = [bin(i) for i in decimal_number]
hexadecimal_number = [hex(i) for i in decimal_number]
print(decimal_number)
print(binary_number)
print(hexadecimal_number)
print("\nUsing slices, we'll now show a portion of each list :")
startNb = int(input("What decimal number would you like to start at : "))
stopNb = int(input("What decimal number would you like to stop at : "))
while (startNb < 1 or startNb > stopNb) or (stopNb < 1 or stopNb > fNb):
    startNb = int(input("What decimal number would you like to start at : "))
    stopNb = int(input("What decimal number would you like to stop at : "))
print("\nDecimal values from "+str(startNb)+" to "+str(stopNb)+" :")
for i in decimal_number[startNb-1:stopNb]:
    print(i)

print("\nBinary values from "+str(startNb)+" to "+str(stopNb)+" :")
for i in binary_number[startNb-1:stopNb]:
    print(i)

print("\nHexadecimal values from "+str(startNb)+" to "+str(stopNb)+" :")
for i in hexadecimal_number[startNb-1:stopNb]:
    print(i)

input("\nPress enter to see all values from 1 to "+str(fNb)+".")
print("Decimal ------ Binary ------ Hexadecimal")
print("----------------------------------------\n")
for i,j,k in zip(decimal_number,binary_number,hexadecimal_number):
    print(i,'------ ',j,'------ ',k)