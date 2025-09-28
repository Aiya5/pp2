#Classes and Objects

#Create Classes---------------------------------------------------
class MyClass:
  x = 5

#Create Oblects----------------------------------------------------
p1 = MyClass()
print(p1.x)

#The __init__() Method----------------------------------------------------------------------------------------------------
#Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#Note: The __init__() method is called automatically every time the class is being used to create a new object.