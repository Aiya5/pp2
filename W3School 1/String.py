#Python Strings
#You can use double or single quotes:

print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#------------------------------------------------------------------------------------------
#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#------------------------------------------------------------------------------------
#Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])
#Note: The first character has index 0.

#Slice From the Start
b = "Hello, World!"
print(b[:5])

#Slice To the End
b = "Hello, World!"
print(b[2:])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#---------------------------------------------------------------------------------------------
#Upper case
a = "Hello, World!"
print(a.upper())

#Lower case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#-------------------------------------------------------------------------------------------------------------------------
#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)
#-----------------------------------------------------------------------------------------------------------------
#String Format

#age = 36
#This will produce an error:
#txt = "My name is John, I am " + age
#print(txt)

#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#-------------------------------------------------------------------------------------------------------
#Python - Escape Characters

#You will get an error if you use double quotes inside a string that is surrounded by double quotes:
#txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
#------------------------------------------------------------------------------------------------------
txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\rWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
#--------------------------------------------------------------------------------------------------------
