import math
import random
from itertools import permutations

# 1. Class with getString and printString-----------------------------------------------------------
class IOString:
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Enter a string: ")
    
    def printString(self):
        print(self.s.upper())
strObj = IOString()     # create object
strObj.getString()      # ask user to enter string
strObj.printString()    # print in uppercase


# 2. Shape and Square---------------------------------------------------------------------------
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length
shape1 = Shape()
print("Shape area:", shape1.area())   # -> 0

square1 = Square(5)
print("Square area:", square1.area())  # -> 25


# 3. Rectangle-------------------------------------------------------------------------------------
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
shape1 = Shape()
print("Shape area:", shape1.area())   # 0

square1 = Square(6)
print("Square area:", square1.area()) # 36

rect1 = Rectangle(4, 7)
print("Rectangle area:", rect1.area()) # 28

# 4. Point class-----------------------------------------------------------------------------
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
p1 = Point(3, 4)
p2 = Point(0, 0)

p1.show()   # Point(3, 4)
p2.show()   # Point(0, 0)

print("Distance:", p1.dist(p2))  # 5.0

p1.move(6, 8)
p1.show()   # Point(6, 8)


# 5. Bank Account--------------------------------------------------------------------------------
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount}, balance = {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, balance = {self.balance}")
acc1 = Account("Alice", 100)   # Create account with 100 balance

print(f"Owner: {acc1.owner}, Balance: {acc1.balance}")

acc1.deposit(50)   # Add 50 → balance = 150
acc1.withdraw(70)  # Withdraw 70 → balance = 80
acc1.withdraw(200) # Too much! → "Insufficient funds!"

#Prime Filter with lambda:-------------------------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Using filter with lambda
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 20]

prime_nums = list(filter(lambda x: is_prime(x), nums))
print("Prime numbers:", prime_nums)