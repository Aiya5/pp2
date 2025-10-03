# 1. Generator that generates squares of numbers up to N--------------------------------------------------------------------------------
def gen_squares(N):
    for i in range(N+1):
        yield i * i

print("Squares up to 5:")
for val in gen_squares(5):
    print(val, end=" ")
print("\n")


#Generator to print even numbers between 0 and n (comma separated)-----------------------------------------------------------------------------------------------------
def gen_evens(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number for even numbers: "))
print(",".join(str(num) for num in gen_evens(n)))


#Generator for numbers divisible by 3 and 4 between 0 and n------------------------------------------------------------------------------------
def div_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("Divisible by 3 and 4 up to 50:")
for num in div_by_3_and_4(50):
    print(num, end=" ")
print("\n")


#Generator squares between a and b--------------------------------------------------------------------------------
def squares(a, b):
    for i in range(a, b+1):
        yield i * i

print("Squares between 3 and 7:")
for val in squares(3, 7):
    print(val, end=" ")
print("\n")


#Generator countdown from n to 0----------------------------------------------------------------------------------
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("Countdown from 5:")
for val in countdown(5):
    print(val, end=" ")
print()
