# Python Built-in Functions — Notes and Examples

# abs() - Returns the absolute value of a number
print("abs(-10) =", abs(-10))

# all() - True if all elements are true
print("all([True, True, False]) =", all([True, True, False]))

# any() - True if any element is true
print("any([False, 0, True]) =", any([False, 0, True]))

# ascii() - Returns readable version of object, escapes non-ascii
print("ascii('ğüşi') =", ascii('ğüşi'))

# bin() - Converts to binary
print("bin(7) =", bin(7))

# bool() - Converts to Boolean
print("bool(0) =", bool(0))

# bytearray() - Returns array of bytes
print("bytearray('hello', 'utf-8') =", bytearray('hello', 'utf-8'))

# bytes() - Returns bytes object
print("bytes('hi', 'utf-8') =", bytes('hi', 'utf-8'))

# callable() - Checks if object is callable
print("callable(print) =", callable(print))

# chr() - Unicode code to character
print("chr(65) =", chr(65))

# classmethod() - Converts a function to class method
class Demo:
    x = 5
    @classmethod
    def show(cls):
        return cls.x
print("classmethod example =", Demo.show())

# compile() - Compiles code into executable object
code = compile('x=5\nprint(x)', '', 'exec')
exec(code)

# complex() - Creates complex number
print("complex(3, 4) =", complex(3, 4))

# delattr() - Deletes the specified attribute from an object
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')
print(x)

# Check again to confirm deletion
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age')

print(x)

# dict() - Creates dictionary
print("dict(a=1, b=2) =", dict(a=1, b=2))

# dir() - Lists attributes/methods of object
print("dir([]) =", dir([]))

# divmod() - Returns (quotient, remainder)
print("divmod(10, 3) =", divmod(10, 3))

# enumerate() - Returns iterable with index
for i, v in enumerate(['a', 'b']): print("enumerate:", i, v)

# eval() - Evaluates expression
print("eval('3 + 5') =", eval('3 + 5'))

# exec() - Executes code dynamically
exec("x = 10\nprint('exec example:', x)")

# filter() - Filters elements by condition
print("filter() =", list(filter(lambda n: n > 2, [1,2,3,4])))

# float() - Converts to float
print("float(5) =", float(5))

# format() - Formats string
print("format(255, 'x') =", format(255, 'x'))

# frozenset() - Immutable set
print("frozenset([1,2,3]) =", frozenset([1,2,3]))

# getattr() - Gets attribute value
class Person: name = "Aiya"
print("getattr(Person, 'name') =", getattr(Person, 'name'))

# globals() - Global variables dictionary
print("globals().keys() contains 'globals'?", 'globals' in globals())

# hasattr() - Checks if object has attribute
print("hasattr(Person, 'name') =", hasattr(Person, 'name'))

# hash() - Returns hash value
print("hash('test') =", hash('test'))

# help() - Help info (commented to avoid long output)
# help(len)

# hex() - Converts to hexadecimal
print("hex(255) =", hex(255))

# id() - Object identity
print("id(5) =", id(5))

# input() - (commented for demo)
# name = input("Enter your name: ")

# int() - Converts to integer
print("int(5.9) =", int(5.9))

# isinstance() - Checks if instance of class
print("isinstance(5, int) =", isinstance(5, int))

# issubclass() - Checks if subclass
class A: pass
class B(A): pass
print("issubclass(B, A) =", issubclass(B, A))

# iter() - Returns iterator
it = iter([1, 2])
print("next(iter()) =", next(it))

# len() - Returns length
print("len('abc') =", len('abc'))

# list() - Converts to list
print("list((1,2,3)) =", list((1,2,3)))

# locals() - Local variables dictionary
def test_locals():
    x = 10
    print("locals() =", locals())
test_locals()

# map() - Applies function to iterable
print("map() =", list(map(str.upper, ['a', 'b'])))

# max() - Returns max value
print("max([1,5,3]) =", max([1,5,3]))

# memoryview() - Returns memory view
print("memoryview(b'hello')[0] =", memoryview(b'hello')[0])

# min() - Returns min value
print("min([4,6,1]) =", min([4,6,1]))

# next() - Next element of iterator
it = iter([1,2,3])
print("next(it) =", next(it))

# object() - Creates new object
print("object() =", object())

# oct() - Converts to octal
print("oct(8) =", oct(8))

# open() - Opens a file (write + read demo)
with open("demo.txt", "w") as f: f.write("Hello")
with open("demo.txt", "r") as f: print("open() =", f.read())

# ord() - Character to Unicode code
print("ord('A') =", ord('A'))

# pow() - Power of numbers
print("pow(2, 3) =", pow(2, 3))

# print() - Prints output
print("print() works!")

# property() - Defines managed attribute
class C:
    def __init__(self): self._x = None
    def getx(self): return self._x
    def setx(self, value): self._x = value
    x = property(getx, setx)
c = C(); c.x = 10
print("property example =", c.x)

# range() - Sequence of numbers
print("range(3) =", list(range(3)))

# repr() - Returns string representation
print("repr('hi') =", repr('hi'))

# reversed() - Reverses sequence
print("reversed('abc') =", list(reversed('abc')))

# round() - Rounds number
print("round(3.678, 2) =", round(3.678, 2))

# set() - Creates a set
print("set([1,2,2,3]) =", set([1,2,2,3]))

# setattr() - Sets attribute value
class D: pass
d = D()
setattr(d, 'age', 20)
print("setattr result =", d.age)

# slice() - Creates slice object
print("slice(1,4) =", [0,1,2,3,4][slice(1,4)])

# sorted() - Returns sorted list
print("sorted([3,1,2]) =", sorted([3,1,2]))

# staticmethod() - Defines static method
class Math:
    @staticmethod
    def add(a,b): return a+b
print("staticmethod example =", Math.add(2,3))

# str() - Converts to string
print("str(123) =", str(123))

# sum() - Sum of iterable
print("sum([1,2,3]) =", sum([1,2,3]))

# super() - Calls parent method
class Parent: 
    def greet(self): return "Hi from Parent"
class Child(Parent): 
    def greet(self): return super().greet() + " & Child"
print("super() example =", Child().greet())

# tuple() - Creates tuple
print("tuple([1,2,3]) =", tuple([1,2,3]))

# type() - Returns type of object
print("type(5) =", type(5))

# vars() - Returns __dict__ of object
print("vars(Math) =", vars(Math))

# zip() - Combines iterables
print("zip() =", list(zip([1,2,3], ['a','b','c'])))
