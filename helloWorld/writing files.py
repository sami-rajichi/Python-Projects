# to create a file and write in it, we have 3 specific characters which are a , w and x
try:
    f = open("demo2.txt", "a")
    f.write("Hello World !")
    f.write("we are writing in file now")
except:
    print("something went wrong")
finally:
    print("writing finished with success")

try:
    f = open("demo2.txt")
    print(f.read())
except:
    print("something went wrong")
finally:
    print("reading finished with success")

try:
    f = open("demo3.txt", "w")
    f.write("Hello World !")
    f.write("we are writing in file now")
except:
    print("something went wrong")
finally:
    print("writing finished with success")