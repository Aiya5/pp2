import os
name = input("Enter filename: ")
text= input("Input text")
if os.path.exists(name):
    open(name, "w").write(open(text).read())
else:
    print("Not found")