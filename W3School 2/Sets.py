#Sets
#* Note: Set items are unchangeable, but you can remove items and add new items.


thisset = {"apple", "banana", "cherry"}
print(thisset)
#------------------------------------------------------------------------------------------
#Set items are unordered, unchangeable, and do not allow duplicate values.
#------------------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#------------------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#------------------------------------------------------------------------------------------
#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

#------------------------------------------------------------------------------------------

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
#------------------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#------------------------------------------------------------------------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#------------------------------------------------------------------------------------------
set1 = {"abc", 34, True, 40, "male"}

print(set1)

#------------------------------------------------------------------------------------------
myset = {"apple", "banana", "cherry"}
print(type(myset))
#------------------------------------------------------------------------------------------

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#------------------------------------------------------------------------------------------
#Access set items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#------------------------------------------------------------------------------------------

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#------------------------------------------------------------------------------------------

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
#------------------------------------------------------------------------------------------
#Add set items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#------------------------------------------------------------------------------------------

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#------------------------------------------------------------------------------------------

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#------------------------------------------------------------------------------------------

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#------------------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#------------------------------------------------------------------------------------------

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#------------------------------------------------------------------------------------------

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#------------------------------------------------------------------------------------------

thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset)
#------------------------------------------------------------------------------------------
#Loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#------------------------------------------------------------------------------------------
#Join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) #Union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) #also union
#------------------------------------------------------------------------------------------

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#------------------------------------------------------------------------------------------

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
#------------------------------------------------------------------------------------------

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#------------------------------------------------------------------------------------------
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) #update

#------------------------------------------------------------------------------------------

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) #intesection
#------------------------------------------------------------------------------------------

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#------------------------------------------------------------------------------------------

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
#------------------------------------------------------------------------------------------

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#------------------------------------------------------------------------------------------

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) #Difference
#------------------------------------------------------------------------------------------

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
#------------------------------------------------------------------------------------------

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#------------------------------------------------------------------------------------------

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) #symmetriic difference
#------------------------------------------------------------------------------------------

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
#------------------------------------------------------------------------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
#------------------------------------------------------------------------------------------
#Frosenset

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#------------------------------------------------------------------------------------------

fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)

#------------------------------------------------------------------------------------------
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b))
print(a - b)

#------------------------------------------------------------------------------------------
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)

#------------------------------------------------------------------------------------------
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))

#------------------------------------------------------------------------------------------
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)
#-------------------------------------------------------------------------------------------
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)

#-------------------------------------------------------------------------------------------
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))
print(a ^ b)

#-------------------------------------------------------------------------------------------
a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)

#-------------------------------------------------------------------------------------------
#Set Methods
#add()-Adds an element to the set
#clear()-Removes all the elements from the set
#copy()-Returns a copy of the set
#difference()-Returns a set containing the difference between two or more sets
#difference_update()-=Removes the items in this set that are also included in another, specified set
#discard()-Remove the specified item
#intersection()-&Returns a set, that is the intersection of two other sets
#intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	 	Returns whether two sets have a intersection or not
#issubset()	<=	Returns True if all items of this set is present in another set
# 	<	Returns True if all items of this set is present in another, larger set
#issuperset()	>=	Returns True if all items of another set is present in this set
# 	>	Returns True if all items of another, smaller set is present in this set
#pop()	 	Removes an element from the set
#remove()	 	Removes the specified element
#symmetric_difference()	^	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
#union()	|	Return a set containing the union of sets
#update()	|=	Update the set with the union of this set and others

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)
#-------------------------------------------------------------------------------------------
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)
#-------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
#-------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
#-------------------------------------------------------------------------------------------
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)
#-------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
#-------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
#-------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
#-------------------------------------------------------------------------------------------
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
#-------------------------------------------------------------------------------------------
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
#-------------------------------------------------------------------------------------------
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)
#-------------------------------------------------------------------------------------------
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)
#-------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
#-------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
#-------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)
#-------------------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)
#-------------------------------------------------------------------------------------------
