# 1. Generator that generates squares of numbers up to N--------------------------------------------------------------------------------
def generate_squares(N):
    for i in range(1, N + 1):
        yield i ** 2  
for square in generate_squares(5):
    print(square)


#Generator to print even numbers between 0 and n (comma separated)-----------------------------------------------------------------------------------------------------
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Enter a number: "))
print(", ".join(str(num) for num in even_numbers(n)))


#Generator for numbers divisible by 3 and 4 between 0 and n------------------------------------------------------------------------------------
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter the limit: "))
for num in divisible_by_3_and_4(n):
    print(num)


#Generator squares between a and b--------------------------------------------------------------------------------
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
for val in squares(2, 6):
    print(val)

#Generator countdown from n to 0----------------------------------------------------------------------------------
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
for num in countdown(5):
    print(num)
