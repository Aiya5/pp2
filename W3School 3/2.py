import math
import random
from itertools import permutations

#Grams → Ounces------------------------------------------------------------------------
def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(100))  # Example: 100 grams → ounces


#Fahrenheit → Celsius-------------------------------------------------------------------------
def fahrenheit_to_celsius(F):
    return (5/9) * (F - 32)

print(fahrenheit_to_celsius(98.6))  # Example: 98.6 F → 37 C


#Chickens & Rabbits puzzle----------------------------------------------------------------------
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2*chickens + 4*rabbits == numlegs:
            return chickens, rabbits
    return None

print(solve(35, 94))  # (23 chickens, 12 rabbits)

#Filter Primes--------------------------------------------------------------------------------------
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

print(filter_prime([1, 2, 3, 4, 5, 11, 15, 19]))

#String permutations---------------------------------------------------------------------------
from itertools import permutations

def string_permutations(s):
    perms = permutations(s)
    for p in perms:
        print(''.join(p))

string_permutations("abc")

#Reverse sentence-----------------------------------------------------------------------------------
def reverse_sentence(s):
    words = s.split()
    return ' '.join(words[::-1])

print(reverse_sentence("We are ready"))

#Reverse words in a sentence--------------------------------------------------------------------------
def reverse_sentence(s):
    words = s.split()
    return ' '.join(words[::-1])

print(reverse_sentence("We are ready"))

#Has 33-------------------------------------------------------------------------------------------
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))        # True
print(has_33([1, 3, 1, 3]))     # False
print(has_33([3, 1, 3]))        # False


#Spy game (007 in order)-----------------------------------------------------------------------------
def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False


#Volume of sphere---------------------------------------------------------------------------------
import math

def sphere_volume(r):
    return (4/3) * math.pi * (r**3)

print(sphere_volume(3))  # radius 3


#Unique list--------------------------------------------------------------------------------------------
def unique_list(lst):
    unique = []
    for x in lst:
        if x not in unique:
            unique.append(x)
    return unique

print(unique_list([1,2,2,3,4,4,5]))

#Palindrome check----------------------------------------------------------------------------------------
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("nurses run"))


#Histogram----------------------------------------------------------------------------------------------
def histogram(lst):
    for n in lst:
        print('*' * n)

histogram([4, 9, 7])


#Guess the Number game----------------------------------------------------------------------------------

def guess_number():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

# guess_number()   # Uncomment to play

