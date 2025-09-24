#Creating new variables
x = 5
y = "John"
print(x)
print(y)

a = 4       # x is of type int
a = "Sally" # x is now of type str
print(a)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#-------------------------------------------------------------------------------------------------------------

#Get The Type
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

a = 4
A = "Sally"

print(a)
print(A)
#----------------------------------------------------------------------------------------------------------------

#Legal names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#illegal names

#2myvar = "John"
#my-var = "John"
#my var = "John"

#This example will produce an error in the result

#Camel case
myVariableName = "John"
#Pascal case
MyVariableName = "John"
#Snake case
my_variable_name = "John"

#------------------------------------------------------------------------------------------------------------------------


#Assign values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#---------------------------------------------------------------------------------------------------------------------

#Outpet variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)  #For numbers, the + character works as a mathematical operator

#x = 5
#y = "John"
#print(x + y) 
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

x = 5
y = "John"
print(x, y)


#----------------------------------------------------------------------------------------------------------

#Global variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#-----------------------------------
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Global keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#--------------------------------
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Thats all 