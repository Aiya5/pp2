#Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#-------------------------------------------------------------------------------------------------
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#-------------------------------------------------------------------------------------------------
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#-------------------------------------------------------------------------------------------------
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#-------------------------------------------------------------------------------------------------
tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

#-------------------------------------------------------------------------------------------------
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#-------------------------------------------------------------------------------------------------
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#-------------------------------------------------------------------------------------------------
#Access tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#-------------------------------------------------------------------------------------------------
#Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)
#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#-------------------------------------------------------------------------------------------------
#Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

#-------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#-------------------------------------------------------------------------------------------------
fruits = ("apple", "banana", "cherry")

print(fruits)
#--------------------------------------------------------------------------------------------------
#Unpack Tuplea
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#--------------------------------------------------------------------------------------------------
#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
#--------------------------------------------------------------------------------------------------
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#--------------------------------------------------------------------------------------------------
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#--------------------------------------------------------------------------------------------------
#Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#--------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#--------------------------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#--------------------------------------------------------------------------------------------------
#Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#--------------------------------------------------------------------------------------------------
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#--------------------------------------------------------------------------------------------------
#Tuple Methods
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
#--------------------------------------------------------------------------------------------------
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)