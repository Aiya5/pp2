import re
txt="write a Python program that replaces all spaces in a string with underscores"
x=re.sub(" ","_",txt)
print(x)