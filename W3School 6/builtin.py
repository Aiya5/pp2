import math
import time

#----------------------------------------------------------------------------------
x = list((1,2,3,4,5,6,7,8,9))
result = math.prod(x)
print(result)

#-----------------------------------------------------------------------------------
text=input("enter string")
upper_case = sum(map(str.isupper, text))
lower_case = sum(map(str.islower, text))
print("Upper", upper_case)
print("Lower", lower_case)

#---------------------------------------------------------------------------------
text=input("enter string ")
new_text= "".join(reversed(text))
print("Is palindrom? ", text==new_text)

#------------------------------------------------------------------------------------------
num = int(input("enter num: "))
milliseconds = int(input("enter milliseconds: "))
time.sleep(milliseconds / 1000) 
result = math.sqrt(num)
print(f"Square root of {num} after {milliseconds} miliseconds is {result}")

#-----------------------------------------------------------------------------------
tuple = (2, "True", 4, 6)
new_tuple = (2, "True", 0, "False")
print(all(tuple))
print(all(new_tuple))

