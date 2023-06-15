# deleting file

import os

if os.path.exists("demo3.txt"):
    os.remove("demo3.txt")
else:
    print("file doesn't exist")

# deleting directory

if os.path.exists("demo"):
    os.rmdir("demo")
else:
    print("directory doesn't exist")