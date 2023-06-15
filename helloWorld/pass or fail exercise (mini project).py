mark = int(input(" Give me your mark"))

if mark > 20 or mark < 0 :
    print("This mark has overtook the scope [0 .. 20]")
elif mark == 20 :
    print("excellent")
elif mark >= 17 :
    print("very good")
elif mark >= 14 :
    print("good")
elif mark >= 10 :
    print("medium")
else:
    print("bad")