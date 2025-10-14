import re

# ----------------------------
#re.findall()
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# ----------------------------
#re.search()
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# ----------------------------
#re.split()
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# ----------------------------
#re.sub()
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# ----------------------------
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)

# ----------------------------
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)

# ----------------------------
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)

# ----------------------------
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

# ----------------------------
txt = "hello planet"
#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

# ----------------------------
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)

# ----------------------------
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)

# ----------------------------
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

# ----------------------------
txt = "hello planet"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x)

# ----------------------------
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# ----------------------------
txt = "Åland"
#Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))
#Without the flag, the example would return all character:
print(re.findall("\w", txt))
#Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A))

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------
# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------
# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------

# ----------------------------
