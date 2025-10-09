# ============================================================
# 🧩 CLASSES
# ============================================================

# 1. Student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# 2. Employee with salary increase
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)


# 3. Animal → Dog
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Woof!")


# 4. Employee → Manager
class Employee2:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"{self.name} and {self.salary}")


class Manager(Employee2):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def info(self):
        print(f"{self.name}, {self.salary}, Department: {self.department}")


# 5. Shape → Circle
import math


class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# 6. Dog sit & bark
class Dog2:
    def sit(self):
        print("Dog is sitting")

    def bark(self, quantity):
        for _ in range(quantity):
            print("Woof!")


# 7. Circle (area and perimeter)
class Circle2:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 8. Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"'{self.title}' by {self.author}")


# 9. Student simple
class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Student {self.name} is {self.age} years old.")


# ============================================================
# 🧮 FUNCTIONS
# ============================================================

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"


def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def max_in_list(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


def sum_of_square_roots(a, b):
    return math.sqrt(a) + math.sqrt(b)


def c_to_f(c):
    return c * 9/5 + 32


# ============================================================
# 🔁 LISTS & LOOPS
# ============================================================

# Even numbers
def print_even_numbers(lst):
    for n in lst:
        if n % 2 == 0:
            print(n)


# Reverse list manually
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list


# Largest number
def largest_number(lst):
    largest = lst[0]
    for n in lst:
        if n > largest:
            largest = n
    return largest


# Uppercase names
def print_uppercase(names):
    for name in names:
        print(name.upper())


# Second largest
def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second


# Sum of list
def sum_list(lst):
    total = 0
    for n in lst:
        total += n
    return total


# Count positive numbers
def count_positive(lst):
    count = 0
    for n in lst:
        if n > 0:
            count += 1
    return count


# Multiply all numbers
def multiply_list(lst):
    result = 1
    for n in lst:
        result *= n
    return result


# ============================================================
# 🧵 STRINGS
# ============================================================

def is_palindrome(word):
    return word == word[::-1]


def replace_spaces(s):
    return s.replace(" ", "-")


def reverse_string(s):
    return s[::-1]


def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join(c for c in s if c not in vowels)


def char_count(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def capitalize_sentence(s):
    return s.title()


def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


def starts_and_ends_same(s):
    return s[0] == s[-1]


def count_digits(s):
    return sum(c.isdigit() for c in s)


# ============================================================
# 📘 DICTIONARIES
# ============================================================

def word_count(sentence):
    words = sentence.split()
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    return count


def countries_and_capitals():
    countries = {"Kazakhstan": "Astana", "Japan": "Tokyo", "France": "Paris"}
    for country, capital in countries.items():
        print(country, "-", capital)


def fruits_cheaper_than_5():
    fruits = {"apple": 3, "banana": 6, "orange": 4}
    for fruit, price in fruits.items():
        if price < 5:
            print(fruit)


def increase_salaries():
    employees = {"Ali": 50000, "Dana": 60000, "Serik": 70000}
    for name in employees:
        employees[name] *= 1.1
    return employees


def people_older_than_18():
    people = {"Ali": 17, "Dana": 20, "Serik": 25}
    for name, age in people.items():
        if age > 18:
            print(name)


# ============================================================
# ✅ TEST SECTION (You can comment out what you don’t need)
# ============================================================

if __name__ == "__main__":
    print("=== CLASS EXAMPLES ===")
    s = Student("Aigerim", 20)
    s.introduce()

    e = Employee("Dana", 50000)
    e.increase_salary(10)
    print("New salary:", e.salary)

    d = Dog("Buddy")
    d.sound()

    m = Manager("Aruzhan", 80000, "HR")
    m.info()

    c = Circle(5)
    print("Circle area:", c.area())

    # Functions
    print("\n=== FUNCTIONS ===")
    print("Hypotenuse:", hypotenuse(3, 4))
    print("Even or Odd:", even_or_odd(5))
    print("Vowels:", count_vowels("Education"))
    print("Max in list:", max_in_list([3, 7, 2, 9, 5]))
    print("Sum of roots:", sum_of_square_roots(4, 9))
    print("Celsius to Fahrenheit:", c_to_f(0))

    # Lists
    print("\n=== LISTS ===")
    print_even_numbers([1, 2, 3, 4, 5, 6])
    print("Reversed:", reverse_list([1, 2, 3, 4]))
    print("Largest:", largest_number([3, 7, 2, 9, 5]))
    print_uppercase(["Ali", "Dana", "Serik"])
    print("Second largest:", second_largest([10, 20, 4, 45, 99]))
    print("Sum:", sum_list([1, 2, 3, 4]))
    print("Positive count:", count_positive([-1, 2, 0, 5, -3]))
    print("Product:", multiply_list([2, 3, 4]))

    # Strings
    print("\n=== STRINGS ===")
    print("Palindrome:", is_palindrome("level"))
    print("Replace spaces:", replace_spaces("Hello world from Python"))
    print("Reverse:", reverse_string("Python"))
    print("Remove vowels:", remove_vowels("Beautiful day"))
    print("Character count:", char_count("banana"))
    print("Capitalized:", capitalize_sentence("hello world from python"))
    print("Longest word:", longest_word("Python is powerful and simple"))
    print("Starts and ends same:", starts_and_ends_same("radar"))
    print("Digit count:", count_digits("abc123xyz45"))

    # Dictionaries
    print("\n=== DICTIONARIES ===")
    print("Word count:", word_count("this is a test this is only a test"))
    countries_and_capitals()
    fruits_cheaper_than_5()
    print("Increased salaries:", increase_salaries())
    people_older_than_18()
