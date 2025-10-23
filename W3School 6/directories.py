import os
#------------------------------------------------------------------------------------------------------
path = input("Enter folder path: ")
if os.path.exists(path):
    print("in folder:", os.listdir(path))
    print("folders:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    print("files:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)
else:
    print("folder doesn't exist")

#------------------------------------------------------------------------------------
path = input("Enter any path: ")
print(f"Path: {path}")
print("Exists?", os.path.exists(path))
print("Can read?", os.access(path, os.R_OK))
print("Can write?", os.access(path, os.W_OK))
print("Can run?", os.access(path, os.X_OK))

#-------------------------------------------------------------------------------------------------
path = input("Enter file path: ")
if os.path.exists(path):
    print("Path is real")
    print("Folder part:", os.path.dirname(path))
    print("File part:", os.path.basename(path))
else:
    print("Path doesn't exist")

#---------------------------------------------------------------------------------------
filename = input("Enter filename: ")
if os.path.exists(filename):
    with open(filename) as f:
        lines = f.readlines()
    print(len(lines))
else:
    print("Not found")
    
#---------------------------------------------------------------------------------------
words = ["Hello", "This", "Is", "A", "Test"]
open("test.txt", "w").write("\n".join(words))
print("Done")

#---------------------------------------------------------------------------------------------
for i in range(26):
    open(chr(65 + i) + ".txt", "w").write("File " + chr(65 + i) + ".txt\n")
print("Done")

#--------------------------------------------------------------------------------------------------
file1 = input("Enter file: ")
file2 = input("Enter file to copy to: ")
if os.path.exists(file1):
    open(file2, "w").write(open(file1).read())
    print("Copied")
else:
    print("No file")

#---------------------------------------------------------------------------------------
path = input("something to delete ")
if not os.path.exists(path):
    print("no such file")
elif not os.access(path, os.W_OK):
    print("Can't delete - no permission")
else:
    os.remove(path)
    print("File deleted")