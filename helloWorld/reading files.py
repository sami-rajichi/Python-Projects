try:
    f = open("demo.txt")
    print(f.read())
except:
    print("something went wrong")
finally:
    print("everything is okay")

try:
    f = open("demo.txt")
    print(f.readline())
    print(f.readline())
    print(f.readline())
except:
    print("something went wrong")
finally:
    print("everything is okay")

try:
    f = open("demo.txt")
    for line in f:
        print(line)
except:
    print("something went wrong")
finally:
    print("everything is okay")

try:
    f = open("demo.txt")
    for line in f:
        line = line.strip("\n")  # we use .strip function to avoid spaces between phases
        print(line)
except:
    print("something went wrong")
finally:
    print("everything is okay")